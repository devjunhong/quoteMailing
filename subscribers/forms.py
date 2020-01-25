from django import forms


class SubscribeForm(forms.Form):  
  name = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)

  def send_email(self):
    print(self.cleaned_data)
      # send email using the self.cleaned_data dictionary
    pass