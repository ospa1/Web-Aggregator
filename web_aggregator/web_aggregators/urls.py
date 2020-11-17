""" Defines url patterns for web_aggregators """

from django.urls import path
from . import views

app_name = 'web_aggregators'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]
