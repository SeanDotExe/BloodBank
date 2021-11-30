from django.urls import path

from . import views

urlpatterns = [
  
  path('', views.index, name='index'),
  path('donor-home.html', views.donor_home, name='donor_home'),
  path('index.html', views.index, name='index'),
  path('donor-donate.html', views.donor_donate, name='donor_donate'),
  path('donor-request.html', views.donor_request, name='donor_request'),
  path('donor-account.html', views.donor_account, name='donor_account'),
]
