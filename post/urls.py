from django.urls import path
from .views import CreatePostView, PostDetailView, PostListView, PostListViewSchool

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='post-detail'),
    path('school/', PostListViewSchool.as_view(), name='post_by_School'),
]
