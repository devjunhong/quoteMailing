from django.forms import ModelForm
from .models import Subscribers


class SubscribeForm(ModelForm):  
  class Meta: 
    model = Subscribers
    exclude = (
      'register_date',
      'activate',
      'subscription',
    )
  
  def is_valid(self):
    print('is_valid')
    print(self.data)
    print(self)
    return True 
  
  def send_email(self):
    print(self.cleaned_data)
      # send email using the self.cleaned_data dictionary
    pass