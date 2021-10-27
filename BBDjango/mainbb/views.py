

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request,"index.html")

def admin(request):
  return render(request,"adminlogin.html")
