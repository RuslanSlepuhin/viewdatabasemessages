
from rest_framework import viewsets
from .models import NewYork
from .serializers import GetAllMessagesSerializer


class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = NewYork.objects.all().order_by('-time_of_public')
    serializer_class = GetAllMessagesSerializer

