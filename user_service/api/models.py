# Django imports
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=220, blank=False)
    last_name = models.CharField(max_length=220, blank=False)
    email_id = models.CharField(max_length=110, blank=False, unique=True)
    phone_number = models.CharField(max_length=10, blank=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.first_name
