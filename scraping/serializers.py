from rest_framework import serializers

from .models import Telegram, NewYork


class GetAllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewYork
        fields = [
            'chat_name',
            'title',
            'body',
            'time_of_public'
            ]