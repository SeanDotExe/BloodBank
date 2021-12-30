from django import forms
from .models import reg_donor_patient,add_reqdonate, add_reqblood
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','first_name','last_name']
class registration_form(forms.ModelForm):
    class Meta:
        model = reg_donor_patient
        fields = '__all__'
class donate_remarks(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = ['remarks']

class add_donate(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = ['username','fullname','age','sex','weight','add','contactnum','disease','bloodtype','status','date_request']


class need_remarks(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['remarks']

class add_need(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['username','patientname','patientage','sex','healthfac','healthfacadd','contactnum','disease','unit','bloodtype','status','date_request']
class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

        
        # {% csrf_token %}
         #     Pawerrr_1201          {{form.as_p}}
        