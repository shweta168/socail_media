from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
app_name = 'twitter'
urlpatterns = [
    # url(r'', views.ManageAppView.as_view(),name="twitindex"),
    url(r'credentials/$', views.CredentialsView.as_view(),name="credentials"),
    url(r'hashsearch/$', views.HashTagSearchView.as_view(),name="hashsearch"),]