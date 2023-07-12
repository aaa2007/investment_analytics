from django.db import models
from django.forms import ModelForm
from .models import Issuer
from .models import Bond
from .models import Position
from django import forms


class IssuerForm(ModelForm):
    class Meta:
        model = Issuer 
#        fields =  ('issuer_name', 'issuer_credit_rating', 'issuer_country_of_risk', 'issuer_sector') 
        fields =  "__all__"
        
 #   widgets = {        
 #      'issuer_name': forms.TextInput(attrs={'class':'form-control'}), 
 #      'issuer_credit_rating': forms.TextInput(attrs={'class':'form-control'}) ,
 #      'issuer_country_of_risk': forms.TextInput(attrs={'class':'form-control'}), 
 #      'issuer_sector': forms.TextInput(attrs={'class':'form-control'}) 
 #     }
    

class SecurityForm(ModelForm):
    class Meta:
        model = Bond 
        fields = "__all__"  
        widgets = {        
         'isin': forms.TextInput(attrs={'style':'width:185px', 'placeholder': 'ISIN'}), 
         'coupon': forms.NumberInput(attrs={'style':'width:185px', 'placeholder': 'Coupon'}),
         'maturity_date': forms.DateTimeInput(attrs={'style':'width:185px', 'placeholder': 'Maturity Date'}),
          'currency_code': forms.TextInput (attrs={'style':'width:185px', 'placeholder': 'Currency'}) 
        }     
        labels = {        

        }     


class PositionForm(ModelForm):
    class Meta:
        model = Position 
        fields = ['instrument','position']

        widgets = {        
         'position': forms.NumberInput(attrs={'style':'width:320px', 'placeholder': 'position'}) 
        }
    

