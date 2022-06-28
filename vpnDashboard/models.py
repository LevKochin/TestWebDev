from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class device(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class profile(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastseen = models.DateTimeField(default=datetime.datetime.now, verbose_name='Последний визит')
    devices = models.ManyToManyField(device, verbose_name='Устройства')

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'


"""Model that contain information about VPN:
name - name of VPN,
status - status of VPN,
coordinates - value for browse server on the map"""
class vpn(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    status = models.CharField(max_length=50, verbose_name='Статус')
    creationTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='Время запуска')
    coordinates = models.CharField(max_length=50, verbose_name='Координаты')
    profiles = models.ManyToManyField(profile)

    class Meta:
        verbose_name_plural = 'VPNs'
        verbose_name = 'VPN'
        ordering = ['-name']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()