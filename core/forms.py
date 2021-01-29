from django import forms
from django.forms import Form, ModelForm

from crispy_forms.helper import FormHelper

from .models import *


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']


class LaneForm(forms.ModelForm):
    class Meta:
        model = Lane
        fields = ['name', 'path', 'is_worked', 'queue_max',]
        