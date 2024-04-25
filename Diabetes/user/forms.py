from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Info, HealthData

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class CredUpdateForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['height', 'weight', 'age','name'] 
        
class AddHealthData(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['glucose_level']