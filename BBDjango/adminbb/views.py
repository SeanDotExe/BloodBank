from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_admin,blood_counter
from mainbb.models import add_reqblood,add_reqdonate
from .forms import registeradmin,patientrejectform,patientapprovedform,donorrejectform,donor_approved_screening_form,donor_screening_form
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
  count_requests= add_reqdonate.objects.filter(status = "Request Sent").count()
  count_pending= add_reqdonate.objects.filter(status = "Pending").count()
  count_approved= add_reqdonate.objects.filter(status = "Approved").count()
  count_reject= add_reqdonate.objects.filter(status = "Reject").count()

  donor = add_reqdonate.objects.filter(status = "Request Sent")
  pendingdonor = add_reqdonate.objects.filter(status = "Pending")
  datas={
    
    'count_requests':count_requests,
    'count_pending':count_pending,
    'count_reject':count_reject,
    'count_approved':count_approved,

    'pending_donor':pendingdonor,
    'donor':donor
  }
  return render(request,"admindonors.html",datas)




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





def defdonorreject(request,id):
  donor_info = add_reqdonate.objects.get(id=id)
  donorform = donorrejectform(request.POST or None, instance=donor_info)
  context = {
        "donorform": donorform,
        "donor": donor_info
        }
    
  if donorform.is_valid():
      donorform.save()
      return redirect("admindonors")

  return render(request,"donor_reject.html",context)


def defdonorapproved_screening(request,id):
  donor_info = add_reqdonate.objects.get(id=id)
  donorform = donor_approved_screening_form(request.POST or None, instance=donor_info)
  context = {
        "donorform": donorform,
        "donor": donor_info
        }
    
  if donorform.is_valid():
      donorform.save()
      return redirect("admindonors")

  return render(request,"donor_approved_for_screening.html",context)

def defdonor_screening(request,id):
  donor_info = add_reqdonate.objects.get(id=id)
  apos_blood_count = blood_counter.objects.values_list('Apos', flat=True).get(pk=1)
  aneg_blood_count = blood_counter.objects.values_list('Aneg', flat=True).get(pk=1)
  bpos_blood_count = blood_counter.objects.values_list('Bpos', flat=True).get(pk=1)
  bneg_blood_count = blood_counter.objects.values_list('Bneg', flat=True).get(pk=1)
  abpos_blood_count = blood_counter.objects.values_list('ABpos', flat=True).get(pk=1)
  abneg_blood_count = blood_counter.objects.values_list('ABneg', flat=True).get(pk=1)
  opos_blood_count = blood_counter.objects.values_list('Opos', flat=True).get(pk=1)
  oneg_blood_count = blood_counter.objects.values_list('Oneg', flat=True).get(pk=1)

  donorform = donor_screening_form(request.POST or None, instance=donor_info)
  
  context = {
        "donorform": donorform,
        "donor": donor_info
        }
    

  if donorform.is_valid():
          #blood_counter.objects.filter(pk=1).update(Apos= apos_blood_count-patient_info.unit)
      donorform.save()
      getstatus = add_reqdonate.objects.values_list('status', flat=True).get(pk=id)
      getbloodtype = add_reqdonate.objects.values_list('bloodtype', flat=True).get(pk=id)
      if getstatus == "Approved":
        if getbloodtype == "A+":
          blood_counter.objects.filter(pk=1).update(Apos= apos_blood_count+donor_info.unit)
        elif getbloodtype == "A-":
          blood_counter.objects.filter(pk=1).update(Aneg= aneg_blood_count+donor_info.unit)
        elif getbloodtype == "B+":
          blood_counter.objects.filter(pk=1).update(Bpos= bpos_blood_count+donor_info.unit)
        elif getbloodtype == "B-":
          blood_counter.objects.filter(pk=1).update(Bneg= bneg_blood_count+donor_info.unit)
        elif getbloodtype == "AB+":
          blood_counter.objects.filter(pk=1).update(ABpos= abpos_blood_count+donor_info.unit)
        elif getbloodtype == "AB-":
          blood_counter.objects.filter(pk=1).update(ABneg= abneg_blood_count+donor_info.unit)
        elif getbloodtype == "O+":
          blood_counter.objects.filter(pk=1).update(Opos= opos_blood_count+donor_info.unit)
        elif getbloodtype == "O-":
          blood_counter.objects.filter(pk=1).update(Oneg= oneg_blood_count+donor_info.unit)

        

      return redirect("admindonors")

  return render(request,"donor_screening.html",context)

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