from django import forms
from .models import reg_admin

class registeradmin(forms.ModelForm):
    class Meta:
        model = reg_admin
        fields = '__all__'