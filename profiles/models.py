from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    """
    A user profile to maintain default order info
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200,null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    town_or_city = models.CharField(max_length=200, null=True, blank=True)
    street_address1 = models.CharField(max_length=200, null=True, blank=True)
    street_address2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.full_name