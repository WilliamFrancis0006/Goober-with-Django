from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
# Add Forms Here

class mainSearchForm(forms.Form):
    userInput = forms.CharField(label=False, required=False)
    userRecording = ArrayField(forms.IntegerField(widget=forms.HiddenInput(), label="userRecording", required = False)) #id="hiddenRecording"
    searchFocus = forms.BooleanField(widget=forms.HiddenInput(), label="searchFocus", required = False) #id="searchFocus"


