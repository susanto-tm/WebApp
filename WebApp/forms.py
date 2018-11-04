from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginFields(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               label='',
                               widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    password = forms.CharField(max_length=10, label='', widget=forms.PasswordInput)
    required_css_class = 'required'


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='',
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username',}))
    first_name = forms.CharField(max_length=30, required=False, label='',
                                 widget=forms.TextInput({
                                     'class': 'form-control',
                                     'placeholder': 'First Name',}))
    last_name = forms.CharField(max_length=30, required=False, label='',
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Last Name',}))
    email = forms.EmailField(max_length=254, label='',
                             widget=forms.TextInput({
                                 'class': 'form-control',
                                 'placeholder': 'Email Address *',}))
    password1 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput({
                                    'placeholder': 'Password'}))
    password2 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput({
                                    'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
