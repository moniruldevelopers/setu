from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.html import format_html

from .models import *



# Register your models here.
from django.utils.html import mark_safe

#my customizations
admin.site.site_header = "UGV BLOOD ADMIN PANEL"
admin.site.site_title = "UGV BLOOD ADMIN PANEL"
admin.site.index_title = "Welcome to UGV BLOOD  PORTAL"

class DonorProfileAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('user', 'full_name', 'blood_group', 'gender', 'phone_number', 'availability', 'last_donation_date',  'profile_picture_preview')
    
    # Add search functionality to search by full_name, blood_group, phone_number, and user (username)
    search_fields = ('user__username', 'full_name', 'blood_group', 'phone_number', 'user__first_name', 'user__last_name')
    
    # Filter the list by blood group and availability
    list_filter = ('blood_group', 'availability', 'gender', 'last_donation_date')
    

    
  
    
    # Custom method to display a preview of the profile picture in the list view
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return mark_safe(f'<img src="{obj.profile_picture.url}" width="50" height="50" style="object-fit:cover;" />')
        return 'No image'
    profile_picture_preview.short_description = 'Profile Picture'
    
    # Optional: Custom method to format the donation date
    def last_donation_date_display(self, obj):
        return obj.last_donation_date.strftime('%Y-%m-%d') if obj.last_donation_date else 'N/A'
    last_donation_date_display.short_description = 'Last Donation Date'
     
admin.site.register(DonorProfile, DonorProfileAdmin)

class SiteInfoAdminForm(ModelForm):
    class Meta:
        model = SiteInfo
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        if SiteInfo.objects.exists() and not self.instance.pk:
            raise ValidationError("Only one SiteInfo instance is allowed.")
        return cleaned_data

class SiteInfoAdmin(admin.ModelAdmin):
    form = SiteInfoAdminForm

admin.site.register(SiteInfo, SiteInfoAdmin)


class SliderAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('short_text_1', 'image_preview')
    
    # Custom method to display image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image'  # Column name for the image preview

# Register the Slider model with the custom admin settings
admin.site.register(Slider, SliderAdmin)

admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'published_at', 'category', 'image_preview')
    
    # Search functionality
    search_fields = ('title', 'description', 'category__name')  # Search by title, description, and category name
    
    # Custom method to display image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image'  # Column name for the image preview

# Register the Blog model with the custom admin settings
admin.site.register(Blog, BlogAdmin)
class GalleryAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'image_preview')
    
    # Custom method to display image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image'  # Column name for the image preview

# Register the Gallery model with the custom admin settings
admin.site.register(Gallery, GalleryAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')  # Change 'created_at' to 'sent_at'
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)

admin.site.register(Contact, ContactAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('name', 'member_id', 'phone_number', 'image_preview')
    
    # Search functionality
    search_fields = ('name', 'member_id', 'phone_number')
    
    # Filter functionality
    list_filter = ('member_id',)
    
    # Custom method to display image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image'

# Register the TeamMember model with the custom admin settings
admin.site.register(TeamMember, TeamMemberAdmin)



