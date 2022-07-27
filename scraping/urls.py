from django.urls import path

from .views import GetAllMessagesView

urlpatterns = [
    path('messages/', GetAllMessagesView.as_view({'get': 'list'})),
]