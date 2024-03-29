from django.contrib.auth.models import User
from django.db import models

from green_medic.apps.base.models import TimeStampedModel
from green_medic.apps.users.choices import GenderTypes, StatusTypes


class Customer(TimeStampedModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveSmallIntegerField(default=0)
    gender = models.PositiveSmallIntegerField(choices=GenderTypes.choices, default=GenderTypes.UNSPECIFIED)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.user.get_username()}"


class Shopkeeper(TimeStampedModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    shop_name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    registration_number = models.CharField(max_length=30, blank=True, null=True)
    nid = models.CharField(max_length=30, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=StatusTypes.choices, default=StatusTypes.PENDING)

    def __str__(self):
        return f"{self.name}, {self.shop_name} {self.user.get_username()}"
