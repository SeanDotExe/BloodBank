from django import forms
from .models import reg_donor_patient,add_reqdonate, add_reqblood

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
        fields = ['username','fullname','age','sex','weight','add','contactnum','disease','unit','bloodtype','status','date_request']


class need_remarks(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['remarks']

class add_need(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = ['username','patientname','patientage','sex','healthfac','healthfacadd','contactnum','disease','unit','bloodtype','status','date_request']