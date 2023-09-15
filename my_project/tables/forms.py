# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Table, Table23, Table26


# create a ModelForm
class NameForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Table
        fields = "__all__"

class NameForm23(forms.ModelForm):
     class Meta:
         model = Table23
         fields = "__all__"

class NameForm26(forms.ModelForm):
     class Meta:
         model = Table26
         fields = "__all__"