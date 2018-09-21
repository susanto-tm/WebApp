from django import forms
from django.contrib.auth.forms import AuthenticationForm


class HomeForms(forms.Form):
    post = forms.CharField()


class LoginFields(AuthenticationForm):
    # Authentication Form Fields
    username = forms.CharField(max_length=254,
                               label='',
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=30, label='', widget=forms.PasswordInput)
    required_css_class = 'required'
