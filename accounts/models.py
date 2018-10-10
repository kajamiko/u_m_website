from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile is just some user's data for the users kind enough to come back ad pay again

class Profile(models.Model):
    """
    Class extending django auth user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length = 40, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, blank=True, null=True)
    street_address1 = models.CharField(max_length=60, blank=True, null=True)
    street_address2 = models.CharField(max_length=60, blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
     
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()