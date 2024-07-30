from django.urls import path
from .views import (CreateMessageView, UserAMessagesListView, JoinAnonChatView, AnonChatDetailView,
                    AmDetailView, AnnonCreateView, AnonChatCreateView, UserAnonChatListView)

urlpatterns = [
    path('acreate/', AnnonCreateView.as_view(), name='annon_create'),
    path('anonchat/create/', AnonChatCreateView.as_view(), name='anonchat-create'),
    path('user/anonchats/', UserAnonChatListView.as_view(), name='user-anonchats'),
    path('anonchat/join/', JoinAnonChatView.as_view(), name='anonchat-join'),
    path('send/<str:chat_id>/message/', CreateMessageView.as_view(), name='create-message'),
    path('anonchat/<int:pk>/', AnonChatDetailView.as_view(), name='anonchat-detail'),
    #path('messages/<int:pk>/', AmDetailView.as_view(), name='user-messages-detail'),
]

