from django.urls import path 

from .views import HomePageView, ActivationPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('activation/', ActivationPageView.as_view(), name='activation')
]