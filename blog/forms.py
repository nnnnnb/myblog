from django import forms
from .import models


class AddForm(forms.Form):
    cominput = forms.CharField()
