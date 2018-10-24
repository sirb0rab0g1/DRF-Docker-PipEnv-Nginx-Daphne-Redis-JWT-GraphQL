from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BasicInformation(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return 'No Username' if self.user == None else self.user.username
