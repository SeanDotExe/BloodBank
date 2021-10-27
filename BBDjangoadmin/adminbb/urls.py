from django.urls import path

from . import views

urlpatterns = [
  path('', views.defadminlogin, name='adminlogin'),
  path('adminaccess.html', views.defadminaccess, name='adminaccess'),
  path('admindonors.html', views.defadmindonors, name='admindonors'),
  path('adminpatient.html', views.defadminpatient, name='adminpatient'),
]
