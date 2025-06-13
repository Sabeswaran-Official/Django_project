from django import forms
from .models import *


class Student_Form(forms.ModelForm):

    class Meta:

        model = Students_data
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'username': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'reg_no': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'course': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'year': forms.Select(attrs={'class': 'form-control backclass'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control backclass'}),
            'gmail_id': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }

        

        
