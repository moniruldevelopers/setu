from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .views import *
from .forms import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def update_profile(request):
    donor_profile = get_object_or_404(DonorProfile, user=request.user)

    if request.method == 'POST':
        form = DonorProfileForm(request.POST, request.FILES, instance=donor_profile)
        if form.is_valid():
            form.save()
            return redirect('my_details')  # Redirect to a profile detail view
    else:
        form = DonorProfileForm(instance=donor_profile)

    return render(request, 'update_profile.html', {'form': form})



@login_required
def my_details(request):
    profile = get_object_or_404(DonorProfile, user=request.user)
    return render(request, 'my_details.html', {'profile': profile})











def handler404(request, exception):
    return render(request, '404.html', status=404)

