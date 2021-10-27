

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request,"index.html")

def donor_home(request):
  return render(request,"donor-home.html")

def donor_donate(request):
  return render(request,"donor-donate.html")

def donor_request(request):
  return render(request,"donor-request.html")

def donor_account(request):
  return render(request,"donor-account.html")
