from django import forms
from .models import reg_donor_patient,add_reqdonate, add_reqblood

class registration_form(forms.ModelForm):
    class Meta:
        model = reg_donor_patient
        fields = '__all__'
class donate(forms.ModelForm):
    class Meta:
        model = add_reqdonate
        fields = '__all__'

class need(forms.ModelForm):
    class Meta:
        model = add_reqblood
        fields = '__all__'
