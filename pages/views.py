from django.views.generic import FormView
from django.shortcuts import render

from subscribers.models import Subscribers
from subscribers.forms import SubscribeForm

# Create your views here.
class HomePageView(FormView):
  form_class = SubscribeForm
  template_name = 'home.html'
  success_url = 'activation'