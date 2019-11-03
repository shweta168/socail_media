from django import forms
from django.contrib.auth.models import User

class CredentialsForm(forms.Form):
    access_token = forms.CharField(required=True,
                                   label="Access Token")
    access_secret = forms.CharField(required=True,
                                   label="Access Secret")
    consumer_key = forms.CharField(required=True,
                                   label="Consumer Key")
    consumer_secret = forms.CharField(required=True,
                                   label="Consumer Secret")

    def clean(self):
        cleaned_data = self.cleaned_data
        print("cleaned_data===",cleaned_data)


class HashTagSearchForm(forms.Form):
    hash_tag = forms.CharField(required=True,
                                   label="Hash Tag")

    def clean(self):
        cleaned_data = self.cleaned_data