from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone


class User(AbstractUser):

    def __str__(self):
        return self.email


class Item(models.Model):
    item_name = models.CharField(max_length=200, default='item')

    class Meta:
        db_table = 'Items'
        managed = True

    def __str__(self):
        return f'{self.item_name}'


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    task_name = models.CharField(max_length=250)
    deadline = models.DateTimeField('deadline', default=timezone.now)
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_to')

    class Meta:
        db_table = 'Event'
        managed = True

    def __str__(self):
        return f'{self.task_name}'


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, db_column='item', null=True, blank=True)
    date_supplied = models.DateField('date supplied')
    quantity = models.PositiveIntegerField(default=0)
    unit_type = models.CharField(max_length=20, default='meters')
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, db_column='event')

    class Meta:
        db_table = 'Inventory'
        verbose_name_plural = 'inventories'
        managed = True

    def __str__(self):
        return f'{self.event}'
