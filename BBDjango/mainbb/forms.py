from django import forms
from .models import reg_donor_patient

class registration_form(forms.ModelForm):
    class Meta:
        model = reg_donor_patient
        fields = '__all__'