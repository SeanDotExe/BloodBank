from django.urls import path

from . import views

urlpatterns = [
  path('', views.defadminlogin, name='adminlogin'),
  path('adminlogin.html', views.defadminlogin, name='adminlogin'),
  path('adminaccess.html', views.defadminaccess, name='adminaccess'),
  path('admindonors.html', views.defadmindonors, name='admindonors'),
  path('adminpatient.html', views.defadminpatient, name='adminpatient'),
  path('patient_reject/<id>/', views.defpatientreject, name='patient_reject'),
  path('patient_approved/<id>/', views.defpatientapproved, name='patient_approved'),
  path('donor_reject/<id>/', views.defdonorreject, name='donor_reject'),
  path('donor_approved_for_screening/<id>/', views.defdonorapproved_screening, name='donor_approved_for_screening'),
  path('donor_screening/<id>/', views.defdonor_screening, name='donor_screening'),
  path('adminregister.html', views.defregister, name='adminregister'),
  path('logout', views.logoutUser, name="logout"),
 # path('patient_approved/<id>/', views.defpatientapproved, name='donor_approved'),
]
