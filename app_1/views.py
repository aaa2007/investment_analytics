
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bond
from .models import Position
from .models import Issuer
from .forms import IssuerForm
from .forms import SecurityForm
from .forms import PositionForm
from django.db.models import Sum
from django.http import HttpResponseRedirect
# Create your views here.




def index(request):
  mypositions = Position.objects.all().order_by('instrument')
  myissuers = Issuer.objects.all().order_by('issuer_name')
  mybonds = Bond.objects.all().order_by('bond_issuer')
  myform = IssuerForm
  template = loader.get_template('index.html')
  context = {'mypositions': mypositions,'myissuers': myissuers,'mybonds': mybonds,'myform':myform}
  return HttpResponse(template.render(context,request))  

def test(request):
    return render(request,'test.html')



def add_issuer(request):
  submitted = False
  if request.method =="POST":
    form = IssuerForm(request.POST)
    if form.is_valid():
      form.save()
      return  HttpResponseRedirect('/app_1/add_issuer/?submitted=True')
  else:
    form = IssuerForm
    if 'submitted' in request.GET:
      submitted = True  

  myform = IssuerForm
  template = loader.get_template('add_issuer.html')
  context = {'myform':myform,'submitted':submitted}
  return HttpResponse(template.render(context,request))  



def add_security(request):
  submitted = False
  if request.method =="POST":
    form = SecurityForm(request.POST)
    if form.is_valid():
      form.save()
      return  HttpResponseRedirect('/app_1/add_security/?submitted=True')
  else:
    form = SecurityForm
    if 'submitted' in request.GET:
      submitted = True  

  myform = SecurityForm
  template = loader.get_template('add_security.html')
  context = {'myform':myform,'submitted':submitted}
  return HttpResponse(template.render(context,request))  

def update_security(request, bond_id):
    mysec = Bond.objects.get(pk=bond_id)
    form = SecurityForm(request.POST or None, instance = mysec)
    if form.is_valid():
           form.save()
           return  HttpResponseRedirect('/app_1/')
    template = loader.get_template('update_security.html')
    context = {'mysec': mysec,'form':form}
    return HttpResponse(template.render(context,request))


def delete_security(request, bond_id):
    mysec = Bond.objects.get(pk=bond_id)
    mysec.delete()
    template = loader.get_template('delete_security.html')
    context = {'mysec': mysec}
    return  HttpResponse(template.render(context,request))




def add_position(request):
  submitted = False
  if request.method =="POST":
    form = PositionForm(request.POST)
    if form.is_valid():
      form.save()
      return  HttpResponseRedirect('/app_1/add_position/?submitted=True')
  else:
    form = PositionForm
    if 'submitted' in request.GET:
      submitted = True  

  myform = PositionForm
  template = loader.get_template('add_position.html')
  context = {'myform':myform,'submitted':submitted}
  return HttpResponse(template.render(context,request))  



def delete_issuer(request, issuer_id):
    myiss = Issuer.objects.get(pk=issuer_id)
    myiss.delete()
    template = loader.get_template('delete_issuer.html')
    context = {'myiss': myiss}
    return  HttpResponse(template.render(context,request))

def update_issuer(request, issuer_id):
    myiss = Issuer.objects.get(pk=issuer_id)
    form = IssuerForm(request.POST or None, instance = myiss)
    if form.is_valid():
           form.save()
           return  HttpResponseRedirect('/app_1/')
    template = loader.get_template('update_issuer.html')
    context = {'myiss': myiss,'form':form}
    return HttpResponse(template.render(context,request))



def delete_position(request, pos_id):
    mypos = Position.objects.get(pk=pos_id)
    mypos.delete()
    template = loader.get_template('delete_position.html')
    context = {'mypos': mypos}
    return  HttpResponse(template.render(context,request))

def update_position(request, pos_id):
    mypos = Position.objects.get(pk=pos_id)
    form = PositionForm(request.POST or None, instance = mypos)
    if form.is_valid():
           form.save()
           return  HttpResponseRedirect('/app_1/')
    template = loader.get_template('update_position.html')
    context = {'mypos': mypos,'form':form}
    return HttpResponse(template.render(context,request))


