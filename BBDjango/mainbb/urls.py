from django.urls import path
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  
  path('', views.index, name='index'),
  path('donor-home.html', views.donor_home, name='donor_home'),
  path('index.html', views.index, name='index'),
  path('donor-donate.html', views.donor_donate, name='donor_donate'),
  path('donor-request.html', views.donor_request, name='donor_request'),
  path('donor-account.html', views.donor_account, name='donor_account'),
  path('register.html', views.user_reg, name='register'),
  path('change-password.html',PasswordsChangeView.as_view(template_name='change-password.html')),
  path('pw-success.html', views.pw_success, name='pw_success'),
  path('logout1', views.logoutUser1, name="logout1"),
]