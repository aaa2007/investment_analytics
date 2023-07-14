from django.db import models
from django.forms import ModelForm
from .models import Issuer
from .models import Bond
from .models import Position
from django import forms


class IssuerForm(ModelForm):
    class Meta:
        model = Issuer 
        fields =  "__all__"
        


class SecurityForm(ModelForm):
    class Meta:
        model = Bond 
        fields = "__all__"  
        widgets = {        
         'isin': forms.TextInput(attrs={'style':'width:155px', 'placeholder': 'ISIN'}), 
         'coupon': forms.NumberInput(attrs={'style':'width:155px', 'placeholder': 'Coupon'}),
         'maturity_date': forms.DateInput(attrs={'style':'width:155px', 'placeholder': 'Maturity Date'}),
          'currency_code': forms.TextInput (attrs={'style':'width:155px', 'placeholder': 'Currency'}) 
        }     


class PositionForm(ModelForm):
    class Meta:
        model = Position 
        fields = ['instrument','position']

        widgets = {        
         'position': forms.NumberInput(attrs={'style':'width:282px', 'placeholder': 'position'}) 
        }
    

