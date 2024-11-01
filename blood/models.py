from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class DonorProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # New field for gender
    date_of_birth = models.DateField()
    phone_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
    )
    present_address = models.TextField(max_length=400)
    permanent_address = models.TextField(max_length=400, blank=True, null=True)
    last_donation_date = models.DateField(blank=True, null=True)
    availability = models.BooleanField(default=True)  # To indicate if they are available for donation

    def __str__(self):
        return f'{self.full_name} ({self.blood_group})'