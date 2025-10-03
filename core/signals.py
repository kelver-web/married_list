from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Gift
from generate_ia.client import generate_gift_description


@receiver(pre_save, sender=Gift)
def add_gift_description(sender, instance, **kwargs):
    if not instance.description:
        instance_description = generate_gift_description(instance.name)
        instance.description = instance_description
