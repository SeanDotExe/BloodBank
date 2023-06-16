from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reg_admin
from mainbb.models import add_reqblood,add_reqdonate,blood_counter
from .forms import registeradmin,patientrejectform,patientapprovedform,donorrejectform,donor_approved_screening_form,donor_screening_form,register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import PasswordChangeView
#from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings
from datetime import date, timedelta
import datetime

def logoutUser(request):
  logout(request)
  return redirect("adminlogin")


def defregister(request):
  form = register()
  if request.method == 'POST':
    form = register(request.POST)
    passwordvalue1= form['password1'].value()
    passwordvalue2= form['password2'].value()
    uservalue= form['username'].value()
    emaill= form['email'].value()
    fname = form['first_name'].value()
    lname = form['last_name'].value()


    if form.is_valid():
      #if User.objects.filter(username=uservalue).exists():
      #user = User.objects.create_user(uservalue, email=emaill, password='johnpassword', is_staff=True)
      User.objects.create_user(uservalue, email=emaill,first_name = fname,last_name = lname, password=passwordvalue2, is_staff=True)
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
  return render(request, "adminregister.html", context)

def defadminlogin(request):
  if request.method == 'POST':
    userr = request.POST.get('username')
    pw = request.POST.get('password')
    user = authenticate(request, username=userr,password=pw)
    if user is not None and user.is_staff == True:
      login(request, user)
      print("pumasok sya")
      return redirect('adminaccess')
    else:
      print("dito sya pumasok")
      messages.info(request,'Invalid Credentials')

  context = {}

  return render(request, 'adminlogin.html',context)
#Adminkunno_1201

#sampledonor
# Sampollang_1201



@login_required(login_url='adminlogin')
def defadminaccess(request):
  if request.user.is_authenticated and request.user.is_staff:
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
  else:
    return redirect('index')


@login_required(login_url='adminlogin')
def defadmindonors(request):
  if request.user.is_authenticated and request.user.is_staff:

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
  else:
    return redirect('adminlogin')




@login_required(login_url='adminlogin')
def defadminpatient(request):
  if request.user.is_authenticated and request.user.is_staff:
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
  else:
    return redirect('adminlogin')




@login_required(login_url='adminlogin')
def defpatientreject(request,id):
  if request.user.is_authenticated and request.user.is_staff:
    patient_info = add_reqblood.objects.get(id=id)
    username_donorform = patient_info.username
    Id = User.objects.get(username=username_donorform).pk
    user = User.objects.get(id=Id)
    user_email = user.email
    patientform = patientrejectform(request.POST or None, instance=patient_info)
    context = {
          "patientform": patientform,
          "patient": patient_info
          }


    if patientform.is_valid():

        patientform.save()
        mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been DECLINED due to some circumstances,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
        subject_mail = "Blood Bank System Request Blood Result"
        mess_mail = mess
        #User.objects.filter(username=uservalue)
        #dito
        receiver_mail = [user_email]
        print(request.user.email)
        send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
        return redirect("adminpatient")

    return render(request,"patient_reject.html",context)
  else:
    return redirect('adminlogin')



def defdonorreject(request,id):
  if request.user.is_authenticated and request.user.is_staff:

    #user_email = request.user.email

   # d = user.objects.filter(username = username_donorform)
    donor_info = add_reqdonate.objects.get(id=id)
    donorform = donorrejectform(request.POST or None, instance=donor_info)

    username_donorform = donor_info.username
    Id = User.objects.get(username=username_donorform).pk
    user = User.objects.get(id=Id)
    user_email = user.email

    context = {
          "donorform": donorform,
          "donor": donor_info
          }

    if donorform.is_valid():
        donorform.save()
        mess = " Good Day !! " + "\n" + "\n" + "\n"  + "This email is to inform you that your donate request has been REJECTED"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
        subject_mail = "Blood Bank System Donate Request Result"
        mess_mail = mess
        #User.objects.filter(username=uservalue)
        #dito
        receiver_mail = [user_email]
        print(request.user.email)
        send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
        return redirect("admindonors")

    return render(request,"donor_reject.html",context)
  else:
    return redirect('adminlogin')





@login_required(login_url='adminlogin')
def defdonor_history(request,id):
  if request.user.is_authenticated and request.user.is_staff:
    donor_info = add_reqdonate.objects.get(id=id)
    usernm = donor_info.username
    donor_username = Q(username = usernm)
    criterion1 = Q(status="Reject")
    criterion2 = Q(status="Approved")
    donor = add_reqdonate.objects.filter((criterion2 | criterion1) & donor_username)
    context= {
        "donor":donor
        }
    return render(request,"donor_history.html",context)
  else:
    return redirect('adminlogin')

def defpatient_history(request,id):
  if request.user.is_authenticated and request.user.is_staff:
    patient_info = add_reqblood.objects.get(id=id)
    usernm = patient_info.patientname
    patient_username = Q(patientname__contains = usernm)
    criterion1 = Q(status="Reject")
    criterion2 = Q(status="Approved")

    patient = add_reqblood.objects.filter((criterion2 | criterion1) & patient_username)
    context= {
        "patient":patient
        }
    return render(request,"patient_history.html",context)
  else:
    return redirect('adminlogin')




@login_required(login_url='adminlogin')
def defdonorapproved_screening(request,id):
  if request.user.is_authenticated and request.user.is_staff:
    donor_info = add_reqdonate.objects.get(id=id)
    dt = date.today() + timedelta(5)

    x = datetime.date(dt.year,dt.month,dt.day)
    dtoday = x.strftime("%b %d %Y")
    donorform = donor_approved_screening_form(request.POST or None, instance=donor_info)
    username_donorform = donor_info.username
    Id = User.objects.get(username=username_donorform).pk
    user = User.objects.get(id=Id)
    user_email = user.email
    context = {
           "dtoday" : dtoday,
          "donorform": donorform,
          "donor": donor_info
        }

    if donorform.is_valid():
        donorform.save()
        mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your donate request has been APPROVED FOR SCREENING, Please go to your respective clinic on "+dtoday+ ", 11:00 am for your Screening, Please do not be late."   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
        subject_mail = "Blood Bank System Donate Request Result"
        mess_mail = mess
        #User.objects.filter(username=uservalue)
        #dito
        receiver_mail = [user_email]
        send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
        return redirect("admindonors")


    return render(request,"donor_approved_for_screening.html",context)
  else:
    return redirect('adminlogin')

@login_required(login_url='adminlogin')
def defdonor_screening(request,id):
  if request.user.is_authenticated and request.user.is_staff:
      donor_info = add_reqdonate.objects.get(id=id)
      username_donorform = donor_info.username
      Id = User.objects.get(username=username_donorform).pk
      user = User.objects.get(id=Id)
      user_email = user.email
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
            blood_counter.objects.filter(pk=1).update(Apos= apos_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "A-":
            blood_counter.objects.filter(pk=1).update(Aneg= aneg_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "B+":
            blood_counter.objects.filter(pk=1).update(Bpos= bpos_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "B-":
            blood_counter.objects.filter(pk=1).update(Bneg= bneg_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "AB+":
            blood_counter.objects.filter(pk=1).update(ABpos= abpos_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "AB-":
            blood_counter.objects.filter(pk=1).update(ABneg= abneg_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "O+":
            blood_counter.objects.filter(pk=1).update(Opos= opos_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
          elif getbloodtype == "O-":
            blood_counter.objects.filter(pk=1).update(Oneg= oneg_blood_count+1)
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your blood donation"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Approved"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
        else:
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "Thank you so much for your time to make an appointment to our clinic, we were sad to say that your screening has been REJECTED due to some circumstances"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Blood Donation Rejected"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("admindonors")
  else:
    return redirect('adminlogin')






  return render(request,"donor_screening.html",context)

@login_required(login_url='adminlogin')
def defpatientapproved(request,id):
  if request.user.is_authenticated and request.user.is_staff:
    apos_blood_count = blood_counter.objects.values_list('Apos', flat=True).get(pk=1)
    aneg_blood_count = blood_counter.objects.values_list('Aneg', flat=True).get(pk=1)
    bpos_blood_count = blood_counter.objects.values_list('Bpos', flat=True).get(pk=1)
    bneg_blood_count = blood_counter.objects.values_list('Bneg', flat=True).get(pk=1)
    abpos_blood_count = blood_counter.objects.values_list('ABpos', flat=True).get(pk=1)
    abneg_blood_count = blood_counter.objects.values_list('ABneg', flat=True).get(pk=1)
    opos_blood_count = blood_counter.objects.values_list('Opos', flat=True).get(pk=1)
    oneg_blood_count = blood_counter.objects.values_list('Oneg', flat=True).get(pk=1)
    mlist = []


    oposd={"O+":opos_blood_count, "O-":oneg_blood_count}
    onegd = {"O-":oneg_blood_count}
    aposd = {"O+":opos_blood_count, "O-":oneg_blood_count,"A+":apos_blood_count, "A-":aneg_blood_count}
    anegd = {"O-":oneg_blood_count, "A-":aneg_blood_count}
    bposd = {"O+":opos_blood_count, "O-":oneg_blood_count,"B+":bpos_blood_count, "B-":bneg_blood_count}
    bnegd = {"O-":oneg_blood_count, "B-":bneg_blood_count}
    abposd = {"O+":opos_blood_count, "O-":oneg_blood_count,"A+":apos_blood_count, "A-":aneg_blood_count,"B+":bpos_blood_count, "B-":bneg_blood_count,"AB+":abpos_blood_count, "AB-":abneg_blood_count}
    abnegd = {"O-":oneg_blood_count,"A-":aneg_blood_count, "B-":bneg_blood_count,"AB-":abneg_blood_count}



    #.objects.filter(pk=survey.pk).update(active=True)
    patient_info = add_reqblood.objects.get(id=id)
    username_donorform = patient_info.username
    Id = User.objects.get(username=username_donorform).pk
    user = User.objects.get(id=Id)
    user_email = user.email
    patientform = patientapprovedform(request.POST or None, instance=patient_info)

    if patient_info.bloodtype == "O+":
        for i in oposd:
            if oposd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "O-":
        for i in onegd:
            if onegd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "A+":
        for i in aposd:
            if aposd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "A-":
        for i in anegd:
            if anegd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "B+":
        for i in bposd:
            if bposd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "B-":
        for i in bnegd:
            if bnegd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "AB+":
        for i in abposd:
            if abposd[i]>=patient_info.unit:
                mlist.append(i)
    elif patient_info.bloodtype == "AB-":
        for i in abnegd:
            if abnegd[i]>=patient_info.unit:
                mlist.append(i)

    if patientform.is_valid():
        if patient_info.bloodtype == "O+":
            blood_counter.objects.filter(pk=1).update(Opos= opos_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "O-":
            blood_counter.objects.filter(pk=1).update(Oneg= oneg_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "A+":
            blood_counter.objects.filter(pk=1).update(Apos= apos_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "A-":
            blood_counter.objects.filter(pk=1).update(Aneg= aneg_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "B+":
            blood_counter.objects.filter(pk=1).update(Bpos= bpos_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "B-":
            blood_counter.objects.filter(pk=1).update(Bneg= bneg_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "AB+":
            blood_counter.objects.filter(pk=1).update(ABpos= abpos_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
        elif patient_info.bloodtype == "AB-":
            blood_counter.objects.filter(pk=1).update(ABneg= abneg_blood_count-patient_info.unit)
            patientform.save()
            mess = " Good Day !! " + "\n" + "\n" + "\n" + "This email is to inform you that your request blood has been ACCEPTED,"   + "\n" + "\n" +"For more info, please visit bloodbanksystem.pythonanywhere.com and login your account"+ "\n" + "\n" + "If you have any questions, please feel free to message us to this email." + "\n" + "\n" + "\n" + "Thank you very much!" + "\n" +  "Regards," + "\n" +"Blood Bank System Administrator"
            subject_mail = "Blood Bank System Request Blood Result"
            mess_mail = mess
            #User.objects.filter(username=uservalue)
            #dito
            receiver_mail = [user_email]
            print(request.user.email)
            send_mail(subject_mail, mess_mail, "bbsystem1201@gmail.com", receiver_mail, fail_silently=False)
            return redirect("adminpatient")
    context = {
          "patientform": patientform,
          "patient": patient_info,
          "mlist" : mlist
          }

    return render(request,"patient_approved.html",context)


  else:
    return redirect('adminlogin')
