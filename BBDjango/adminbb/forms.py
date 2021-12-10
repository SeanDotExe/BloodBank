from django import forms
from .models import reg_admin
from mainbb.models import add_reqblood,add_reqdonate

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

