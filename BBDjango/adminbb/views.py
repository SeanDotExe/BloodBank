from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_admin,blood_counter
from mainbb.models import add_reqblood,add_reqdonate
from .forms import registeradmin,patientrejectform,patientapprovedform
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
  needblood = add_reqblood.objects.filter(status = "Request Sent")
  apos_blood_count = blood_counter.objects.values_list('Apos', flat=True).get(pk=1)
  aneg_blood_count = blood_counter.objects.values_list('Aneg', flat=True).get(pk=1)
  bpos_blood_count = blood_counter.objects.values_list('Bpos', flat=True).get(pk=1)
  bneg_blood_count = blood_counter.objects.values_list('Bneg', flat=True).get(pk=1)
  abpos_blood_count = blood_counter.objects.values_list('ABpos', flat=True).get(pk=1)
  abneg_blood_count = blood_counter.objects.values_list('ABneg', flat=True).get(pk=1)
  opos_blood_count = blood_counter.objects.values_list('Opos', flat=True).get(pk=1)
  oneg_blood_count = blood_counter.objects.values_list('Oneg', flat=True).get(pk=1)

  datas ={
     'needblood':needblood,
     'apos_blood_count':apos_blood_count,
     'aneg_blood_count':aneg_blood_count,
     'bpos_blood_count':bpos_blood_count,
     'bneg_blood_count':bneg_blood_count,
     'abpos_blood_count':abpos_blood_count,
     'abneg_blood_count':abneg_blood_count,
     'opos_blood_count':opos_blood_count,
     'oneg_blood_count':oneg_blood_count,
    }

  return render(request,"adminpatient.html",datas)


def defpatientreject(request,id):
  patient_info = add_reqblood.objects.get(id=id)
  patientform = patientrejectform(request.POST or None, instance=patient_info)
  context = {
        "patientform": patientform,
        "patient": patient_info
        }
    
  if patientform.is_valid():
      patientform.save()
      return redirect("adminpatient")

  return render(request,"patient_reject.html",context)

def defpatientapproved(request,id):
  apos_blood_count = blood_counter.objects.values_list('Apos', flat=True).get(pk=1)
  aneg_blood_count = blood_counter.objects.values_list('Aneg', flat=True).get(pk=1)
  bpos_blood_count = blood_counter.objects.values_list('Bpos', flat=True).get(pk=1)
  bneg_blood_count = blood_counter.objects.values_list('Bneg', flat=True).get(pk=1)
  abpos_blood_count = blood_counter.objects.values_list('ABpos', flat=True).get(pk=1)
  abneg_blood_count = blood_counter.objects.values_list('ABneg', flat=True).get(pk=1)
  opos_blood_count = blood_counter.objects.values_list('Opos', flat=True).get(pk=1)
  oneg_blood_count = blood_counter.objects.values_list('Oneg', flat=True).get(pk=1)
  #.objects.filter(pk=survey.pk).update(active=True)
  patient_info = add_reqblood.objects.get(id=id)
  patientform = patientapprovedform(request.POST or None, instance=patient_info)
  context = {
        "patientform": patientform,
        "patient": patient_info
        }
  print(patient_info.bloodtype)
  print(patient_info.bloodtype)
  if patientform.is_valid():
    if patient_info.bloodtype == "A+":
      blood_counter.objects.filter(pk=1).update(Apos= apos_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "A-":
      blood_counter.objects.filter(pk=1).update(Aneg= aneg_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "B+":
      blood_counter.objects.filter(pk=1).update(Bpos= bpos_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "B-":
      blood_counter.objects.filter(pk=1).update(Bneg= bneg_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "AB+":
      blood_counter.objects.filter(pk=1).update(ABpos= abpos_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "AB-":
      blood_counter.objects.filter(pk=1).update(ABneg= abneg_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "O+":
      blood_counter.objects.filter(pk=1).update(Opos= opos_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")
    elif patient_info.bloodtype == "O-":
      blood_counter.objects.filter(pk=1).update(Oneg= oneg_blood_count-patient_info.unit)
      patientform.save()
      return redirect("adminpatient")

  return render(request,"patient_approved.html",context)