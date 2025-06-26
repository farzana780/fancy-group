from django import forms
from .models import Job_Apply


class Job_Form(forms.ModelForm):
    class Meta:
        model = Job_Apply
        fields = ['full_name', 'email_address', 'phone_number', 'file']
