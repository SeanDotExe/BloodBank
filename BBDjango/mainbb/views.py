

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_donor_patient
from .forms import registration_form,donate,need
from operator import itemgetter
from django.contrib import messages

def index(request):
  form = registration_form(request.POST or None)
  if form.is_valid():
    form.save()
  context = {'form': form}
  return render(request,"index.html",context)

def donor_home(request):
  return render(request,"donor-home.html")

def donor_donate(request):
  formdonate = donate(request.POST or None)
  if formdonate.is_valid():
    formdonate.save()
    messages.success(request, "Form successfully submitted")
  context1 = {'formdonate': formdonate}
  return render(request,"donor-donate.html",context1 )

def donor_request(request):
  formdonate = need(request.POST or None)
  if formdonate.is_valid():
    formdonate.save()
    messages.success(request, "Form successfully submitted")
  context2 = {'formdonate': formdonate}
  return render(request,"donor-request.html", context2)

def donor_account(request):
  return render(request,"donor-account.html")
