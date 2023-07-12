from django.db import models
from datetime import date
import numpy as np

day_count_base = 365
valuation_date = date.today()

class Issuer(models.Model):
   issuer_name =  models.CharField(max_length=100)
   issuer_credit_rating =  models.CharField(max_length=100)
   issuer_country_of_risk= models.CharField(max_length=100)
   issuer_sector= models.CharField(max_length=100)

   def __str__(self):
     return f"{self.issuer_name}"
      
class Bond(models.Model):
   isin = models.CharField(max_length=100)
   bond_issuer =  models.ForeignKey(Issuer, on_delete =models.CASCADE)
   maturity_date  = models.DateField()
   coupon =  models.FloatField()
   currency_code = models.CharField(max_length=3)

 
   @property
   def time_to_maturity(self):
     ttm =((self.maturity_date - valuation_date).days)/day_count_base
     return  ttm   

   @property
   def yield_to_maturity(self):
     miny = 2
     cc= self.coupon
     yy = np.maximum(cc*np.exp(np.random.standard_normal()/5),miny)# randomness mimicks market data feeds, just to show functionality
     return  yy  

   @property
   def price(self):
     y= self.yield_to_maturity/100
     T = self.time_to_maturity
     c = self.coupon/100
     px = c*(1-np.exp(-y*T))/y + np.exp(-y*T)
     return  px*100

   @property
   def duration(self):
    # placeholder: simple example 
     y= self.yield_to_maturity/100
     T = self.time_to_maturity
     duration =  (1-np.exp(-y*T))/y 
     return  duration

   def __str__(self):
     return f"{self.bond_issuer}  {self.coupon}  {self.maturity_date}   {self.currency_code}"


class Position(models.Model):
  position =  models.FloatField()
  instrument = models.ForeignKey(Bond, on_delete=models.CASCADE)
 
  @property
  def dv01(self):
        return  

  def __str__(self):
     return f"{self.instrument}  {round(self.position,0)}"



