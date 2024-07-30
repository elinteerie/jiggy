from rest_framework import serializers
from .models import AMessages, Annon, AnonChat

class AnnonCreateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Annon
        fields = ['id', 'annon_user', 'annon_username']
        read_only_fields = ['annon_user']

class AnonChatSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    class Meta:
        model = AnonChat
        fields = ['id', 'annon_user', 'chat', 'group', 'messages']
        read_only_fields = ['chat', 'annon_user', 'pass_code']

    def get_messages(self, obj):
        request = self.context.get('request')
        messages = obj.message.all()
        paginator = self.context.get('paginator')
        paginated_messages = paginator.paginate_queryset(messages, request)
        serializer = AMessagesSerializer(paginated_messages, many=True)
        return serializer.data


class AMessagesSerializer(serializers.ModelSerializer):

    annon_username = serializers.CharField(source='annon_user.annon_username', read_only=True)
    class Meta:
        model = AMessages
        fields = ['annon_username','content', 'time_created']
        read_only_fields = ['time_created']


class AnonChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonChat
        fields = ['id', 'annon_user', 'chat', 'message', 'pass_code', 'group']

class JoinAnonChatSerializer(serializers.Serializer):
    pass_code = serializers.CharField(max_length=6)
