from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *

# Register your models here.
admin.site.register(DonorProfile)


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


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('short_text_1', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Gallery)