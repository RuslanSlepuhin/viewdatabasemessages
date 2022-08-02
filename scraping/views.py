from django.core.paginator import Paginator
from django.db.models import Max
from rest_framework import viewsets
from .models import Channels, Participant, TelegramChannelsProfessions
from .serializers import GetAllMessagesSerializer, GetAllUsersSerializer, GetAllChannelsSerializer


class GetAllChannelsView(viewsets.ModelViewSet):
    queryset = Channels.objects.all().order_by('-id')
    serializer_class = GetAllChannelsSerializer

class GetAllUsersView(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('-id')
    serializer_class = GetAllUsersSerializer

class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.all().order_by('-id')
    serializer_class = GetAllMessagesSerializer
    paginator = Paginator(queryset, 100)

class GetBackendView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='backend').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetLookingForView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(title=
                                                          '#Вакансия #Информационные технологии (ИТ), '
                                                          'Украина #Информационные технологии (ИТ), '
                                                          'Украина #Account Manager, Украина #Украина (общий) '
                                                          '#Украина (общий) #Product / Project Manager, Украина')
    serializer_class = GetAllMessagesSerializer

class GetDeveloperView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='developer').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetDevOpsView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='devops').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetPMView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='pm').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetDesignerView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='designer').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetAnalystView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='analyst').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetQAView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='qa').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetHRView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='hr').order_by('-id')
    serializer_class = GetAllMessagesSerializer

class GetADView(viewsets.ModelViewSet):
    queryset = TelegramChannelsProfessions.objects.filter(profession='ad').order_by('-id')
    serializer_class = GetAllMessagesSerializer

