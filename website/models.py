from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='name')
    updated_at = models.DateTimeField('date updated', default=timezone.now)
    email = models.EmailField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        managed = True

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def dump(self):
        fields = {
            'id': self.pk,
            'username': self.username,
            'first_name': str(self.first_name).title(),
            'last_name': str(self.last_name).title(),
            'email': self.email,
            'group': str(self.groups.first()),
            'updated_at': self.updated_at.strftime("%B %d, %Y, %H:%M %p"),
            'last_login': self.last_login
        }
        if self.last_login is not None:
            fields['last_login'] = self.last_login.strftime("%B %d, %Y, %H:%M %p")
        return fields


class Item(models.Model):
    item_name = models.CharField(max_length=200, default='item')

    class Meta:
        db_table = 'Items'
        managed = True

    def __str__(self):
        return f'{self.item_name}'


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, db_column='item', null=True, blank=True)
    date_supplied = models.DateTimeField('date supplied', default=timezone.now)
    quantity = models.PositiveIntegerField(default='0')
    event = models.CharField(max_length=350, default='event')

    class Meta:
        db_table = 'Inventories'
        managed = True

    def __str__(self):
        return f'{self.event}'
