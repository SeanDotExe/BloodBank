

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse



def adminaccess(request):
  return render(request,"adminaccess.html")

def admindonors(request):
  return render(request,"admindonors.html")

def adminlogin(request):
  return render(request,"adminlogin.html")

def adminpatient(request):
  return render(request,"adminpatient.html")
