from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import AMessages, Annon, AnonChat
from .serializers import (AMessagesSerializer, AnnonCreateSerialzer, 
                          AnonChatSerializer, AnonChatListSerializer, JoinAnonChatSerializer)
from rest_framework.pagination import PageNumberPagination



class AnnonCreateView(generics.CreateAPIView):
    queryset = Annon.objects.all()
    serializer_class = AnnonCreateSerialzer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        print(user)
        serializer.save(annon_user=user)



class AnonChatCreateView(generics.CreateAPIView):
    queryset = AnonChat.objects.all()
    serializer_class = AnonChatSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        user = self.request.user

        annon_user =get_object_or_404(Annon, annon_user=user)
        print(user)
        serializer.save(annon_user=annon_user)



class CreateMessageView(generics.CreateAPIView):
    serializer_class = AMessagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        annon = request.user.annon  # Assuming each user has an associated Annon instance
        anon_chat = get_object_or_404(AnonChat, chat=kwargs['chat_id'])
        
        if annon == anon_chat.annon_user or annon in anon_chat.joiners.all():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            message = serializer.save(annon_user=annon)
            anon_chat.message.add(message)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)



class UserAMessagesListView(generics.ListAPIView):
    serializer_class = AMessagesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        annon_username = self.kwargs.get('annon_username')
        # Find Annon object by username
        try:
            annon = Annon.objects.get(Annon_username=annon_username)
            return AMessages.objects.filter(annon_user=annon)
        except Annon.DoesNotExist:
            return AMessages.objects.none()
    
class AmDetailView(generics.RetrieveAPIView):
    queryset = AMessages.objects.all()
    serializer_class = AMessagesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAnonChatListView(generics.ListAPIView):
    serializer_class = AnonChatListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        annon_user =get_object_or_404(Annon, annon_user=user)
        return AnonChat.objects.filter(annon_user=annon_user)
    

class JoinAnonChatView(generics.CreateAPIView):
    serializer_class = JoinAnonChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        annon = request.user.annon  # Assuming each user has an associated Annon instance
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        pass_code = serializer.validated_data['pass_code']
        anon_chat = get_object_or_404(AnonChat, pass_code=pass_code)
        
        if anon_chat:
            anon_chat.joiners.add(annon)
            return Response({"detail": "Joined successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid pass code"}, status=status.HTTP_400_BAD_REQUEST)
        


class AnonChatPagination(PageNumberPagination):
    page_size = 10  # Set the page size for pagination

class AnonChatDetailView(generics.RetrieveAPIView):
    queryset = AnonChat.objects.all()
    serializer_class = AnonChatSerializer
    pagination_class = AnonChatPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['paginator'] = self.pagination_class()
        return context
