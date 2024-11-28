from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

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





class SiteInfo(models.Model):
    site_name = models.CharField(max_length=20)
    site_logo = models.ImageField(upload_to='logo/')
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    site_facebook = models.URLField(max_length=100)
    site_x = models.URLField(max_length=100)
    site_instagram = models.URLField(max_length=100)
    site_pinterest = models.URLField(max_length=100)

    def __str__(self):
        return self.site_name

    def clean(self):
        if SiteInfo.objects.exists() and not self.pk:
            raise ValidationError("Only one SiteInfo instance is allowed.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving
        super().save(*args, **kwargs)


class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')
    short_text_1 = models.CharField(max_length=255)
    short_text_2 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slider: {self.short_text_1}"
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title
    



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the form is submitted

    def __str__(self):
        return f"Message from {self.name} ({self.subject})"
    


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    member_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='team_members/')
    bio = models.TextField(blank=True, null=True)  # Optional field for a bio or description of the team member

    def __str__(self):
        return self.name
    


