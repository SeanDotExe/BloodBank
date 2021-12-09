from django.shortcuts import render
from django.http import HttpResponse

def defadminlogin(request):
  return render(request,"adminlogin.html")
  
def defadminlogin2(request):
  return render(request,"adminlogin.html")

def defadminaccess(request):
  return render(request,"adminaccess.html")

def defadmindonors(request):
  return render(request,"admindonors.html")

def defadminpatient(request):
  return render(request,"adminpatient.html")