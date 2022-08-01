from django.urls import path

from .views import GetAllChannelsView, GetAllUsersView, GetAllMessagesView

urlpatterns = [
    path('channels/', GetAllChannelsView.as_view({'get': 'list'})),
    path('users/', GetAllUsersView.as_view({'get': 'list'})),
    path('messages/', GetAllMessagesView.as_view({'get': 'list'})),
]