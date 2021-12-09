from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_admin,blood_counter
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
  apos_blood_count = blood_counter.objects.values_list('Apos', flat=True).get(pk=1)
  aneg_blood_count = blood_counter.objects.values_list('Aneg', flat=True).get(pk=1)
  bpos_blood_count = blood_counter.objects.values_list('Bpos', flat=True).get(pk=1)
  bneg_blood_count = blood_counter.objects.values_list('Bneg', flat=True).get(pk=1)
  abpos_blood_count = blood_counter.objects.values_list('ABpos', flat=True).get(pk=1)
  abneg_blood_count = blood_counter.objects.values_list('ABneg', flat=True).get(pk=1)
  opos_blood_count = blood_counter.objects.values_list('Opos', flat=True).get(pk=1)
  oneg_blood_count = blood_counter.objects.values_list('Oneg', flat=True).get(pk=1)
  get_count = {
    'apos_blood_count' : apos_blood_count,
    'aneg_blood_count' : aneg_blood_count,
    'bpos_blood_count' : bpos_blood_count,
    'bneg_blood_count' : bneg_blood_count,
    'abpos_blood_count' : abpos_blood_count,
    'abneg_blood_count' : abneg_blood_count,
    'opos_blood_count' : opos_blood_count,
    'oneg_blood_count' : oneg_blood_count,
  }
  return render(request,"adminaccess.html",get_count)

def defadmindonors(request):
  return render(request,"admindonors.html")


def defadminpatient(request):
  return render(request,"adminpatient.html")

def defpatientreject(request):
  return render(request,"patient_reject.html")