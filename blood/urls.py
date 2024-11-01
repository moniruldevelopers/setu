from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [  
    path('',home, name='home'),
    path('profile/', my_details, name='my_details'),
    path('profile/update/', update_profile, name='update_profile'),

]
 