from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .views import *
from .forms import *
from django.shortcuts import render
from django.core.paginator import Paginator

from datetime import date
from django.db.models import Q




# Create your views here.
def home(request):
    site_info = SiteInfo.objects.first()  # Get the first (and only) instance
    sliders = Slider.objects.all().order_by('-created_at')[:5]
    blogs = Blog.objects.all().order_by('-date')[:3]  # Show only 6 blogs on the homepage, you can adjust this
    context = {
        'site_info': site_info,
        'sliders':sliders,
        'blogs': blogs,
    }
    return render(request, 'home.html', context)

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

    # Filter available donors first (only those with availability=True)
    donors = DonorProfile.objects.filter(availability=True)

    # Apply additional filters based on blood group and location
    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if location:
        donors = donors.filter(present_address__icontains=location)

    # Calculate the date 4 months ago
    four_months_ago = datetime.now().date() - timedelta(days=4 * 30)  # Roughly 4 months (30 days each)

    # Filter donors who last donated at least 4 months ago
    donors = donors.filter(last_donation_date__lte=four_months_ago)

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







def blog_list_view(request):
    search_query = request.GET.get('search', '')  # Get search query from the GET request
    blogs = Blog.objects.all().order_by('-date')  # Latest blogs first

    if search_query:
        blogs = blogs.filter(title__icontains=search_query)  # Filter blogs by title using case-insensitive search

    categories = Category.objects.all()
    
    # Pagination
    paginator = Paginator(blogs, 3)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    blogs_page = paginator.get_page(page_number)

    total_blogs = blogs.count()  # Get the total number of blogs

    context = {
        'blogs': blogs_page,  # Paginated blogs
        'categories': categories,
        'total_blogs': total_blogs,  # Total blogs count
        'search_query': search_query,  # Pass the search query to retain it in the input field
    }
    return render(request, 'blog_list.html', context)


def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)  # Fetch the blog post by ID
    category = blog.category  # Get the category of the blog post
    category_blog_count = Blog.objects.filter(category=category).count()  # Get the number of blogs in that category
    all_categories = Category.objects.all()[:20]  # Get all categories (limit to 20)

    # Context
    context = {
        'blog': blog,
        'category': category,
        'category_blog_count': category_blog_count,
        'all_categories': all_categories,
    }
    return render(request, 'blog_detail.html', context)

def blog_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Get the category
    blogs = Blog.objects.filter(category=category).order_by('-date')  # Get blogs for that category
    all_categories = Category.objects.all()[:20]  # Get all categories (limit to 20)

    # Context
    context = {
        'blogs': blogs,
        'category': category,
        'all_categories': all_categories,
    }
    return render(request, 'blog_category_list.html', context)




def gallery_view(request):
    # Fetch all gallery images, ordered by 'id' or 'title'
    gallery_images = Gallery.objects.all().order_by('id')  # Or use 'title' if preferred

    # Set up pagination
    paginator = Paginator(gallery_images, 1)  # Show 1 image per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'gallery.html', context)


def handler404(request, exception):
    return render(request, '404.html', status=404)

