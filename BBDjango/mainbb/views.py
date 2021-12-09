

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_donor_patient,add_reqdonate,add_reqblood
from .forms import registration_form,donate_remarks,need_remarks,add_donate,add_need
from operator import itemgetter
from django.contrib import messages

def index(request):
  form = registration_form(request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, "Successfully Registered")
  context = {'form': form}
  return render(request,"index.html",context)

def donor_home(request):
  return render(request,"donor-home.html")

def donor_donate(request):
  formdonate = add_donate(request.POST or None) 
  if formdonate.is_valid():
    
    formdonate.save()
    
    messages.success(request, "Form successfully submitted")
  context1 = {'formdonate': formdonate}
  return render(request,"donor-donate.html",context1)

def donor_request(request):
  formrequest = add_need(request.POST or None)
  if formrequest.is_valid():
    formrequest.save()
    
    messages.success(request, "Form successfully submitted")
  context2 = {'formrequest': formrequest}
  return render(request,"donor-request.html", context2)



def donor_account(request):
  donate_history_db = add_reqdonate.objects.all()
  need_history_db = add_reqblood.objects.all()

  count_req_need= add_reqblood.objects.filter(status = "Request Sent").count()
  count_req_donor= add_reqdonate.objects.filter(status = "Request Sent").count()
  count_req_total = count_req_need+ count_req_donor

  count_pending_need= add_reqblood.objects.filter(status = "Pending").count()
  count_pending_donor= add_reqdonate.objects.filter(status = "Pending").count()
  count_pending_total = count_pending_need+ count_pending_donor
    
  count_reject_need= add_reqblood.objects.filter(status = "Reject").count()
  count_reject_donor= add_reqdonate.objects.filter(status = "Reject").count()
  count_reject_total = count_reject_need+ count_reject_donor

  count_approved_need= add_reqblood.objects.filter(status = "Approved").count()
  count_approved_donor= add_reqdonate.objects.filter(status = "Approved").count()
  count_approved_total = count_approved_need+ count_approved_donor


  getdata ={
    'donate_data': donate_history_db,
    'need_data': need_history_db,
    'count_req_total': count_req_total,
    'count_pending_total': count_pending_total,
    'count_reject_total': count_reject_total,
    'count_approved_total': count_approved_total
    }
  return render(request,"donor-account.html",getdata)





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