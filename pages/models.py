from django.db import models


class Clients(models.Model):
  email = models.EmailField() 
  register_date = models.DateField(auto_now_add=True)
  # activation 이메일 보내기 
  activate = models.BooleanField()
  # 비활성화 링크 포함하기 
  subscription = models.BooleanField()
