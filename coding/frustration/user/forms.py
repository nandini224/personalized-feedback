from django import forms

from user.models import RegistrationModel


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields =('firstname','lastname','userid','password','mobilenumber','emailid','gender',)
