from django.contrib import admin

# Register your models here.


#from . models import Person
from . models import Bond
from . models import Issuer
from . models import Position

#admin.site.register(Person)
admin.site.register(Bond)
admin.site.register(Issuer)
admin.site.register(Position)
