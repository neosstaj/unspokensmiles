from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import DonationType

@receiver(post_migrate)
def donate_type_olustur(sender,**kwargs):
    if sender.name =='user_app':
        initial_objects = [
            {'title':'Tek Seferlik'},
            {'title':'Aylık'}
        ]
        for obj_data in initial_objects:
            DonationType.objects.get_or_create(**obj_data)
