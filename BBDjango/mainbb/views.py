

# Create your views here.
from django.contrib.messages.api import success
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .models import reg_donor_patient,add_reqdonate,add_reqblood
from .forms import registration_form,donate_remarks,need_remarks,add_donate,add_need,register,PasswordChangingForm
from operator import itemgetter
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm

    success_url = reverse_lazy('pw_success')
  

@login_required(login_url='index')
def pw_success(request):
  if request.user.is_authenticated:
    return render(request, "pw-success.html",{})
  else:
    return redirect('index')



  
def user_reg(request):
  form = register()
  if request.method == 'POST':
    form = register(request.POST)
    passwordvalue1= form['password1'].value()
    passwordvalue2= form['password2'].value()
    uservalue= form['username'].value()
    emaill= form['email'].value()

    if form.is_valid():
      #if User.objects.filter(username=uservalue).exists():
      form.save()
      messages.success(request, "Successfully Registered Please click 'Home' at the Menu Panel to Login")
          
      #else:
       # messages.info(request,"Username already taken, Please fillout another username")
    else:
      if User.objects.filter(username=uservalue).exists():
        messages.info(request,"Username Already Taken: "+"Please fillout another username")
      else:
        messages.info(request, "Password Error:")
        messages.info(request, "~Please check if the Passwords are the same")
        messages.info(request, "~Your Password can't be too similar to your personal information")
        messages.info(request, "~Your Password must contain 8 characters(Letters, Digits and @/./+/-/_ only)")
        messages.info(request, "~Your Password can't be a commonly used password")
        messages.info(request, "~Your Password can't be entirely numeric")
  context = {
            'form': form
        }
  return render(request, "register.html", context)




def index(request):
      if request.method == 'POST':
        userr = request.POST.get('username')
        pw = request.POST.get('password') 
        selected_project_user = {'username':userr}
        user = authenticate(request, username=userr,password=pw)
        if user is not None and user.is_staff == False:
          login(request, user)
          print("pumasok sya")
          return redirect('donor_home')
        else:
          print("dito sya pumasok")
          messages.info(request,'Invalid Credentials')
        
      context = {}

      return render(request, 'index.html',context)





@login_required(login_url='index')
def donor_home(request):
  if request.user.is_authenticated:
    return render(request,"donor-home.html")
  else:
    return redirect('index')



@login_required(login_url='index')
def donor_donate(request):
  if request.user.is_authenticated:
  
    formdonate = add_donate(request.POST or None) 
    if formdonate.is_valid():
      
      formdonate.save()
      
      messages.success(request, "Form successfully submitted")
    context1 = {'formdonate': formdonate}
    return render(request,"donor-donate.html",context1)
  else:
    return redirect('index')


@login_required(login_url='index')
def donor_request(request):
  if request.user.is_authenticated:
    formrequest = add_need(request.POST or None)
    if formrequest.is_valid():
      formrequest.save()
      user = User.objects.get(username=request.user.username)
      print(user)
      messages.success(request, "Form successfully submitted")
    context2 = {'formrequest': formrequest}
    return render(request,"donor-request.html", context2)
  else:
    return redirect('index')




@login_required(login_url='index')
def donor_account(request):
  if request.user.is_authenticated:
    user1 = User.objects.get(username=request.user.username)
    donate_history_db = add_reqdonate.objects.filter(username = user1)
    need_history_db = add_reqblood.objects.filter(username = user1)
    count_req_need= add_reqblood.objects.filter(status = "Request Sent",username = user1).count()
    count_req_donor= add_reqdonate.objects.filter(status = "Request Sent",username = user1).count()
    count_req_total = count_req_need+ count_req_donor

    count_pending_need= add_reqblood.objects.filter(status = "Pending",username = user1).count()
    count_pending_donor= add_reqdonate.objects.filter(status = "Pending",username = user1).count()
    count_pending_total = count_pending_need+ count_pending_donor
      
    count_reject_need= add_reqblood.objects.filter(status = "Reject",username = user1).count()
    count_reject_donor= add_reqdonate.objects.filter(status = "Reject",username = user1).count()
    count_reject_total = count_reject_need+ count_reject_donor

    count_approved_need= add_reqblood.objects.filter(status = "Approved",username = user1).count()
    count_approved_donor= add_reqdonate.objects.filter(status = "Approved",username = user1).count()
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
  else:
    return redirect('index')


def logoutUser1(request):
  logout(request)
  return redirect("index")


#def defadminlogin(request):
#  return render(request,"adminlogin.html")
  
#def defadminlogin2(request):
#  return render(request,"adminlogin.html")

#def defadminaccess(request):
#  return render(request,"adminaccess.html")

#def defadmindonors(request):
#  return render(request,"admindonors.html")

#def defadminpatient(request):
#  return render(request,"adminpatient.html")