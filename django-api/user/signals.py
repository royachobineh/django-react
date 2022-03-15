from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Location, User
from django.core.cache import cache


@receiver(post_save, sender=Location)
def clear_cache(sender, instance, **kwargs):
    print('hello')
    cache.clear()