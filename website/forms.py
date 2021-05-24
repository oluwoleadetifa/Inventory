import website.models as models
from django import forms
from django.forms import ModelForm, NumberInput, TextInput, EmailInput, CharField, DateField


class AddEventForm(ModelForm):
    name = forms.CharField(help_text="enter known staff username", required=True)
