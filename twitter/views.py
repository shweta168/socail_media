from django.shortcuts import render
import json
import requests
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from requests_oauthlib import OAuth1
from . import forms
from .models import TwitterCredentials
from django.shortcuts import render


# Create your views here.

class CredentialsView(generic.FormView):
    template_name = "credentials.html"
    form_class = forms.CredentialsForm
    success_url = reverse_lazy("twitter:hashsearch")

    # model = TwitterCredentails


    def form_valid(self, form):
        access_token = self.request.POST['access_token']
        access_secret = self.request.POST['access_secret']
        consumer_key = self.request.POST['consumer_key']
        consumer_secret = self.request.POST['consumer_secret']
        try:
            tc = TwitterCredentials.objects.get(user=self.request.user)
            tc.access_token = access_token,
            tc.access_secret = access_secret,
            tc.consumer_key = consumer_key,
            tc.consumer_secret = consumer_secret
            tc.save()

        except TwitterCredentials.DoesNotExist:
            tc = TwitterCredentials(
                user=self.request.user,
                access_token=access_token,
                access_secret=access_secret,
                consumer_key=consumer_key,
                consumer_secret=consumer_secret)

            tc.save()
        return super(CredentialsView, self).form_valid(form)


class HashTagSearchView(generic.TemplateView):
    template_name = "hashtag_search.html"
    form_class = forms.HashTagSearchForm
    success_url = reverse_lazy("twitter:hashsearch")

    # def form_valid(self, form, **kwargs):
    #     return super(HashTagSearchView, self).form_valid(form,)

    def get(self, request, *args, **kwargs):
        print("here")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print("here")
        form = self.form_class(request.POST)
        if form.is_valid() and self.request.POST.get('hash_tag'):
            hash_tag = self.request.POST['hash_tag']
            text_list = []
            url = "https://api.twitter.com/1.1/search/tweets.json?q=" + hash_tag + "&count=2"

            t = TwitterCredentials.objects.get(user=self.request.user)
            t1 = (t.consumer_key.encode("ascii"), t.consumer_secret.encode("ascii"),
                  t.access_token.encode("ascii"), t.access_secret.encode("ascii"))

            try:
                headeroauth = OAuth1(*t1)
                # signature_type='auth_header')
                response = requests.get(url, auth=headeroauth)
                content = json.loads(response.content.decode('utf-8'))
                for comment in content['statuses']:
                    text_list.append(comment.get('text'))
                print("text===",text_list)
            except Exception as e:
                import traceback
                print(traceback.format_exc())
        return render(request, self.template_name,
                      {'form': form,'text_list':text_list})

# Create your views here.
