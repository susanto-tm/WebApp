from django import forms
from django.contrib.auth.forms import AuthenticationForm


class HomeForms(forms.Form):
    post = forms.CharField()



class LoginFields(AuthenticationForm):
    # Authentication Form Fields
    username = forms.CharField(max_length = 254,
                               label='Email',
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email',}))
    password = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))