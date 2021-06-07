import website.models as models
from django import forms
from django.forms import ModelForm, HiddenInput, DateInput, TextInput, NumberInput, Select
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    name = forms.CharField(help_text="enter staff username", required=True)

    class Meta:
        model = models.User
        fields = ['name', 'password']

    def save(self, commit=True):
        user = super(UserForm, self).save(co1mmit=False)
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user


class InventoryForm(ModelForm):
    item = forms.ModelChoiceField(queryset=None, widget=HiddenInput(), required=True)
    quantity = forms.IntegerField(widget=NumberInput(
        attrs={
            'class': 'form-control', 'min': 0
        }), required=True)
    unit_type = forms.CharField(widget=TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'example: meters'
        }
    ), required=True)
    event = forms.ModelChoiceField(queryset=None, widget=HiddenInput(), required=True)
    date_supplied = forms.DateField(input_formats=['%m/%d/%Y'], widget=DateInput(attrs={
        'class': 'form-control', 'type': 'date'
    }), required=True)

    class Meta:
        model = models.Inventory
        fields = ['item', 'quantity', 'unit_type', 'event', 'date_supplied']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = models.Item.objects.all()
        self.fields['event'].queryset = models.Event.objects.all()


class EventForm(ModelForm):
    created_by = forms.ModelChoiceField(queryset=None, widget=HiddenInput(), required=True)
    task_name = forms.CharField(widget=TextInput(
        attrs={
            'class': 'form-control'
        }), required=True)
    deadline = forms.DateField(input_formats=['%m/%d/%Y'], widget=DateInput(
        attrs={
            'class': 'form-control', 'type': 'date'
        }), required=True)
    assigned_to = forms.ModelChoiceField(queryset=None, widget=Select(
        attrs={
            'class': 'form-control'
        }), required=True)

    class Meta:
        model = models.Event
        fields = ['created_by', 'task_name', 'deadline', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].queryset = models.User.objects.all()
        self.fields['assigned_to'].queryset = models.User.objects.all()


class ItemForm(ModelForm):
    item_name = forms.CharField(widget=TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Item Name'
        }), required=True)

    class Meta:
        model = models.Item
        fields = ['item_name']
