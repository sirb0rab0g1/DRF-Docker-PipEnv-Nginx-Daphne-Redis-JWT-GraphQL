"""
from django.contrib import admin

from .models import BasicInformation


@admin.register(BasicInformation)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = (
        'user__username',
        'user__email',
    )

    list_display = ('user')
"""
