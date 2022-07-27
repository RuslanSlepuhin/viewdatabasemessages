from rest_framework import serializers

from .models import Telegram


class GetAllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telegram
        fields = [
            'chat_name',
            'title',
            'body',
            'time_of_public'
            ]