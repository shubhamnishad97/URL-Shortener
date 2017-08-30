from django import forms

class SubmitUrl(forms.Form):
    url=forms.CharField(label="Submit URL")