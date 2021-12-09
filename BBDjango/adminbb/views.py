from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_admin
from .forms import registeradmin
from django.contrib import messages
def defadminlogin(request):
  form = registeradmin(request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, "Successfully Registered")
  context = {'form': form}
  return render(request,"adminlogin.html",context)
  
def defadminlogin2(request):
  return render(request,"adminlogin.html")

def defadminaccess(request):
  return render(request,"adminaccess.html")

def defadmindonors(request):
  return render(request,"admindonors.html")

def defadminpatient(request):
  return render(request,"adminpatient.html")