from django import forms
from django.utils import timezone
from .models import DonorProfile

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ['full_name', 'profile_picture', 'blood_group', 'gender', 'date_of_birth',
                  'phone_number', 'present_address', 'permanent_address',
                  'last_donation_date', 'availability']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'last_donation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'availability': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_last_donation_date(self):
        last_donation_date = self.cleaned_data.get('last_donation_date')
        today = timezone.now().date()

        if last_donation_date and last_donation_date > today:
            raise forms.ValidationError("You cannot select a date in the future for the last donation date. Today is allowed.")

        return last_donation_date
