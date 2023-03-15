from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=200)

class Register(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()