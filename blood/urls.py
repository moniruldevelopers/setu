from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [  
    path('',home, name='home'),
    path('manage-profile/', manage_profile, name='manage_profile'),
    path('profile/', my_details, name='my_details'),
    

]
 