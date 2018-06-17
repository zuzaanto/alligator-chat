from django.db import models
from django.contrib.auth.models import User as UserDef
# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserDef)
    def __str__(self):
        return self.name

class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(UserDef, on_delete=models.CASCADE)
    pub_date = models.DateField()
