from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ConversationView.as_view(), name='conversation'),
]