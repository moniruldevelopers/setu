from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [  
    path('',home, name='home'),
    path('manage-profile/', manage_profile, name='manage_profile'),
    path('profile/', my_details, name='my_details'),
    path('donors/', donor_list, name='donor_list'),
    path('blogs/', blog_list_view, name='blog_list'),
    path('blog/<int:blog_id>/', blog_detail_view, name='blog_detail'),
    path('category/<int:category_id>/', blog_category_view, name='blog_category'),
    path('gallery/', gallery_view, name='gallery'),


    

]
 