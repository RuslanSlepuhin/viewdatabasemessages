from django.urls import path

from .views import GetAllMessagesView, CreateMessageView

urlpatterns = [
    path('messages/', GetAllMessagesView.as_view({'get': 'list'})),
    path('mmm/', CreateMessageView.as_view()),
]