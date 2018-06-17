from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse

from .models import User, Conversation, Message

def index(request):
    return HttpResponse("Hello, world.")

class ConversationView(generic.ListView):
    template_name = 'chat/conv.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Conversation.objects.order_by('-pub_date')
