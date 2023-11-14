from django import forms
from .models import User
class Create_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','password']