from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse

from .models import User, Conversation, Message

class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    context_object_name = 'conversations_list'
    def get_queryset(self):
        return Conversation.objects.order_by('-name')

class ConversationView(generic.ListView):
    template_name = 'chat/conv.html'
    context_object_name = 'messages_list'

    def get_queryset(self):
        return Message.objects.order_by('-pub_date')
