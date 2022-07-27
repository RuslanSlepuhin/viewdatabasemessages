import asyncio
import configparser
import time

from rest_framework.response import Response
from telethon.sync import TelegramClient
from telethon import functions, types, events, client
from rest_framework import generics, viewsets
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest

from links import list_links
from .models import Telegram

from .serializers import GetAllMessagesSerializer


class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = Telegram.objects.all().order_by('-time_of_public')
    serializer_class = GetAllMessagesSerializer