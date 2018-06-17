from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField('User')

class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField()