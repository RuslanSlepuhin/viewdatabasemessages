
from rest_framework import viewsets
from .models import Channels, Participant, TelegramChannelsProfessions
from .serializers import GetAllMessagesSerializer, GetAllUsersSerializer, GetAllChannelsSerializer


class GetAllChannelsView(viewsets.ModelViewSet):
    queryset = Channels.objects.all()
    serializer_class = GetAllChannelsSerializer

class GetAllUsersView(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = GetAllUsersSerializer

class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.all()
    serializer_class = GetAllMessagesSerializer