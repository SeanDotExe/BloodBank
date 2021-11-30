

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_donor_patient
from .forms import registration_form

def index(request):
  return render(request,"index.html")

def donor_home(request):
  return render(request,"donor-home.html")

def donor_donate(request):

  form = registration_form(request.POST or None)
  if form.is_valid():
    form.save()

  context = {
      'form': form
    }
  return render(request,"donor-donate.html",context )

def donor_request(request):
  return render(request,"donor-request.html")

def donor_account(request):
  return render(request,"donor-account.html")
