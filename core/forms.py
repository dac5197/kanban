from django import forms
from django.forms import Form, ModelForm

from crispy_forms.helper import FormHelper

from .models import *
from .utils import get_card_form_lane_choices


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']


class LaneForm(forms.ModelForm):
    class Meta:
        model = Lane
        fields = ['name', 'path', 'is_worked', 'queue_max',]
        

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

        widgets = {     
            #Set fields to readonly (disabled)
            'number' : forms.TextInput(attrs={'readonly':'readonly'}),
            'created' : forms.DateTimeInput(attrs={'readonly':'readonly'}, format='%m/%d/%Y %H:%M'),
            'updated' : forms.DateTimeInput(attrs={'readonly':'readonly'}, format='%m/%d/%Y %H:%M'),           
            'lane_timestamp' : forms.DateTimeInput(attrs={'readonly':'readonly'}, format='%m/%d/%Y %H:%M'),
            'owner' : forms.TextInput(attrs={'readonly':'readonly'}),
        }

    #Set form field labels, select choices, and required attribute
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)
        #Get lane choices
        self.fields['lane'].choices = get_card_form_lane_choices(card=instance)
