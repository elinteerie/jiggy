from rest_framework import serializers
from .models import Post, ContentType, Comment
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','institution','pred_name']  # Specify the fields you want to return
        depth =1

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    upvote_count = serializers.IntegerField(read_only=True)
    downvote_count = serializers.IntegerField(read_only=True)
    content_type = serializers.CharField()  # Allow input for content_type
    class Meta:
        model = Post
        fields = ['content', 'privacy', 'headline', 'content_type', 'time_created', 'user', 'upvote_count', 'downvote_count', 'share_count', 'boosted']
        read_only_fields = ['id','time_created', 'user', 'upvote_count', 'downvote_count', 'share_count', 'boosted']

    def create(self, validated_data):
        content_type_name = validated_data.pop('content_type').lower()  # Convert to lowercase
        # Check if the content type exists
        content_type, created = ContentType.objects.get_or_create(name=content_type_name)
        validated_data['content_type'] = content_type
        return super().create(validated_data)

    def update(self, instance, validated_data):
        content_type_name = validated_data.pop('content_type', None)
        if content_type_name:
            content_type_name = content_type_name.lower()  # Convert to lowercase
            # Check if the content type exists
            content_type, created = ContentType.objects.get_or_create(name=content_type_name)
            instance.content_type = content_type
        return super().update(instance, validated_data)
    

class UserPredNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pred_name']


class CommentSerializer(serializers.ModelSerializer):
    user = UserPredNameSerializer(read_only=True)
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'parent', 'replies', 'time_created']
        read_only_fields = ['id', 'post', 'user', 'time_created', 'replies' ]