from django.db import models
from django.contrib.auth.models import User

class BasicInformation(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    def __str__(self):
        return self.user.username
