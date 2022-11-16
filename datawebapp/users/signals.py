from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_logged_in)
def update_status_on_login(sender, user, **kwargs):
    user.profile.status = True
    user.profile.save()


@receiver(user_logged_out)
def update_status_on_logout(sender, user, **kwargs):
    if user:
        user.profile.status = False
        user.profile.save()
