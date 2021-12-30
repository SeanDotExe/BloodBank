from django import forms
from .models import reg_admin
from mainbb.models import add_reqblood,add_reqdonate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','first_name','last_name']
class registeradmin(forms.ModelForm):
    class Meta:
        model = reg_admin
        fields = '__all__'

class patientrejectform(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['status','remarks']


class patientapprovedform(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['bloodtype','status','remarks']


class donorrejectform(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = ['status','remarks']

class donor_approved_screening_form(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = ['status','remarks']

        
class donor_screening_form(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = ['id','fullname','weight','disease','bloodtype','status','remarks']