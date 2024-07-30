from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(privacy=False)
    

class PostListViewSchool(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user__institution=user.institution)
    


class PostUpvoteView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        if post.upvotes.filter(id=user.id).exists():
            post.upvotes.remove(user)
            message = "You have removed your upvote."
        else:
            post.upvotes.add(user)
            post.downvotes.remove(user)  # Ensure a post cannot be both upvoted and downvoted
            message = "You have upvoted this post."

        post.save()
        return Response({'status': message, 'upvote_count': post.upvote_count, 'downvote_count': post.downvote_count})

class PostDownvoteView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        if post.downvotes.filter(id=user.id).exists():
            post.downvotes.remove(user)
            message = "You have removed your downvote."
        else:
            post.downvotes.add(user)
            post.upvotes.remove(user)  # Ensure a post cannot be both downvoted and upvoted
            message = "You have downvoted this post."

        post.save()
        return Response({'status': message, 'upvote_count': post.upvote_count, 'downvote_count': post.downvote_count})
    


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        post_id = self.kwargs.get('post_id')
        print(post_id)
        parent_id = self.kwargs.get('parent_id', None)
        post = generics.get_object_or_404(Post, id=post_id)
        parent = generics.get_object_or_404(Comment, id=parent_id) if parent_id else None
        serializer.save(user=self.request.user, post=post, parent=parent)



class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = generics.get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post, parent=None)
    

    

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    