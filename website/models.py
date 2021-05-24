from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.save(using=self.db)
        return user_obj

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            **kwargs,
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    staff = models.BooleanField(default=True)
    superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField('staff status', default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    def is_superuser(self):
        return self.superuser


class Item(models.Model):
    item_name = models.CharField(max_length=200, default='item')

    class Meta:
        db_table = 'Items'
        managed = True

    def __str__(self):
        return f'{self.item_name}'


class Event(models.Model):
    task_name = models.CharField(max_length=250)
    deadline = models.DateTimeField('deadline', default=timezone.now)
    User = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='name', null=True, blank=True)

    class Meta:
        db_table = 'Event'
        managed = True

    def __str__(self):
        return f'{str.title}'


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, db_column='item', null=True, blank=True)
    date_supplied = models.DateTimeField('date supplied', default=timezone.now)
    quantity = models.PositiveIntegerField(default='0')
    unit_type = models.CharField(max_length=20, default='meters')
    event = models.CharField(max_length=350, default='event')

    class Meta:
        db_table = 'Inventory'
        managed = True

    def __str__(self):
        return f'{self.event}'
