from django import forms

class NumberForm(forms.Form):
    firstnumber=forms.IntegerField(max_value=999999999,max_value=1,label="FirstNumber")
    secondnumber=forms.IntegerField(max_value=99999999,min_value=1,label="SecondNumber")
