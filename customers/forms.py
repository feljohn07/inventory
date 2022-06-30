from django import forms

class CustomerForm(forms.Form):
    first_name = forms.CharField(label='Firstname', max_length=125)