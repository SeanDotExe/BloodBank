from django.urls import path

from . import views

urlpatterns = [
  path('', views.defadminlogin, name='adminlogin'),
  path('adminlogin.html', views.defadminlogin2, name='adminlogin'),
  path('adminaccess.html', views.defadminaccess, name='adminaccess'),
  path('admindonors.html', views.defadmindonors, name='admindonors'),
  path('adminpatient.html', views.defadminpatient, name='adminpatient'),
  path('patient_reject/<id>/', views.defpatientreject, name='patient_reject'),
  path('patient_approved/<id>/', views.defpatientapproved, name='patient_approved'),
]
