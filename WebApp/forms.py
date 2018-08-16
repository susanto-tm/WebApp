from django import forms


class HomeForms(forms.Form):
    post = forms.CharField()
