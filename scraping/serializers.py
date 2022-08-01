from rest_framework import serializers

from .models import Channels, Participant, TelegramChannelsProfessions

class GetAllChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = '__all__'

class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class GetAllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramChannelsProfessions
        fields = '__all__'