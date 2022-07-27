import asyncio
import configparser
import time

from rest_framework.response import Response
from rest_framework.views import APIView
from telethon.sync import TelegramClient
from telethon import functions, types, events, client
from rest_framework import generics, viewsets
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest

from links import list_links
from .models import Telegram, NewYork

from .serializers import GetAllMessagesSerializer


class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = NewYork.objects.all().order_by('-time_of_public')
    serializer_class = GetAllMessagesSerializer


class CreateMessageView(APIView):

    serializer_class = GetAllMessagesSerializer

    def post_f(self, request):
        rd = Telegram.objects.create(request.data)

        return Response({'new post': GetAllMessagesSerializer(rd).data})


