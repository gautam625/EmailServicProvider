from django.db import models


class User(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)

class Mail(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()