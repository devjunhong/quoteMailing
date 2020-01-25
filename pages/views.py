from django.views.generic import FormView
from django.shortcuts import render

from subscribers.models import Subscribers

# Create your views here.
class HomePageView(FormView):
  
  template_name = 'home.html'
  