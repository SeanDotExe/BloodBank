from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('adminaccess.html', views.adminaccess, name='adminaccess'),
  path('admindonors.html', views.admindonors, name='admindonors'),
  path('adminlogin.html', views.adminlogin, name='adminlogin'),
  path('adminpatient.html', views.adminpatient, name='adminpatient'),
]
