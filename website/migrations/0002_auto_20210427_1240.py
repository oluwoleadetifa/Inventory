# Generated by Django 3.1.7 on 2021-04-27 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]