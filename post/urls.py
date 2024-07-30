from django.urls import path
from .views import (CreatePostView, PostDetailView, PostListView, PostListViewSchool,
                    PostUpvoteView, PostDownvoteView, CommentCreateView, CommentListView, CommentDetailView)

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='post-detail'),
    path('school/', PostListViewSchool.as_view(), name='post_by_School'),
    path('<int:pk>/upvote/', PostUpvoteView.as_view(), name='post-upvote'),
    path('<int:pk>/downvote/', PostDownvoteView.as_view(), name='post-downvote'),
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('<int:post_id>/comments/add/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:post_id>/comments/<int:parent_id>/reply/', CommentCreateView.as_view(), name='comment-reply'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]

