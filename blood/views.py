from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .views import *
from .forms import *

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import DonorProfile
from datetime import date
from django.db.models import Q




# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def manage_profile(request):
    try:
        donor_profile = DonorProfile.objects.get(user=request.user)
        is_new_profile = False
    except DonorProfile.DoesNotExist:
        donor_profile = None
        is_new_profile = True

    if request.method == 'POST':
        form = DonorProfileForm(request.POST, request.FILES, instance=donor_profile)
        if form.is_valid():
            donor_profile = form.save(commit=False)
            if is_new_profile:
                donor_profile.user = request.user  # Associate the new profile with the logged-in user
            donor_profile.save()
            messages.success(request, "Your profile has been saved successfully!")
            return redirect('my_details')  # Redirect to a profile detail view
    else:
        form = DonorProfileForm(instance=donor_profile)

    return render(request, 'manage_profile.html', {'form': form, 'is_new_profile': is_new_profile})


@login_required
def my_details(request):
    try:
        profile = DonorProfile.objects.get(user=request.user)
    except DonorProfile.DoesNotExist:
        # Redirect to the manage_profile page if no donor profile exists
        return redirect('manage_profile')  # Adjust this if your URL name is different

    return render(request, 'my_details.html', {'profile': profile})






def donor_list(request):
    # Get filter parameters
    blood_group = request.GET.get('blood_group', '')
    location = request.GET.get('location', '')

    # Filter donors based on search criteria
    donors = DonorProfile.objects.all()

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if location:
        donors = donors.filter(present_address__icontains=location)

    # Order the donors to avoid warning
    donors = donors.order_by('full_name')

    # Add calculation for days since last donation
    for donor in donors:
        if donor.last_donation_date:
            # Convert datetime.now() to date to match the donor's last donation date
            today = datetime.now().date()
            donor.days_since_last_donation = (today - donor.last_donation_date).days
        else:
            donor.days_since_last_donation = None

    # Paginate the results
    paginator = Paginator(donors, 5)  # Show 5 donors per page
    page = request.GET.get('page')
    donors = paginator.get_page(page)

    # Add context to pass to the template
    context = {
        'donors': donors,
        'blood_groups': DonorProfile.BLOOD_GROUP_CHOICES,
        'is_search': bool(blood_group or location),
    }

    return render(request, 'donor_list.html', context)




def handler404(request, exception):
    return render(request, '404.html', status=404)

