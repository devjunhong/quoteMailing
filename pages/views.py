from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy

from subscribers.models import Subscribers
from subscribers.forms import SubscribeForm

# Create your views here.
class HomePageView(FormView):
  form_class = SubscribeForm
  template_name = 'home.html'
  success_url = reverse_lazy('activation')

  def form_valid(self, form): 
    print('form_valid') 
    return super().form_valid(form)


class ActivationPageView(TemplateView):
  template_name = 'activation.html'