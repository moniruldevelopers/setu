from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .views import *
from .forms import *
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










def handler404(request, exception):
    return render(request, '404.html', status=404)

