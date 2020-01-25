from django.views.generic import FormView, TemplateView
from django.shortcuts import render

from subscribers.models import Subscribers
from subscribers.forms import SubscribeForm

# Create your views here.
class HomePageView(FormView):
  form_class = SubscribeForm
  template_name = 'home.html'
  success_url = 'activation'

  def form_valid(self): 
    print('form_valid') 


class ActivationPageView(TemplateView):
  template_name = 'activation.html'