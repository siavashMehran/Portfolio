from django import forms
from django.forms import widgets
from .models import ContactMe

class ContactMeForm(forms.ModelForm):

    class Meta:
        model   = ContactMe
        fields  = ['name', 'email', 'messege', 'phone']      