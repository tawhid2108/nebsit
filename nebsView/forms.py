from django.forms import ModelForm
from django import forms
from .models import Client





class ClientForm(forms.ModelForm):
   

    class Meta:
        model = Client
        fields = ('fullName', 'email', 'phone', 'message')


        widgets = {

            'fullName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' :  forms.EmailInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control'}),
           
            


        }