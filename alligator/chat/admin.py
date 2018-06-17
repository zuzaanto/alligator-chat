from django.contrib import admin
from django.contrib.auth.models import User

from .models import Conversation, Message

# admin.site.register(User)
admin.site.register(Conversation)
admin.site.register(Message)
