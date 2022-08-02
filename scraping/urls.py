from django.urls import path

from .views import GetAllChannelsView, GetAllUsersView, GetAllMessagesView, GetBackendView, GetLookingForView, \
    GetDeveloperView, GetDevOpsView, GetPMView, GetDesignerView, GetAnalystView, GetQAView, GetHRView, GetADView

urlpatterns = [
    path('channels/', GetAllChannelsView.as_view({'get': 'list'})),
    path('users/', GetAllUsersView.as_view({'get': 'list'})),
    path('messages/', GetAllMessagesView.as_view({'get': 'list'})),
    path('backend/', GetBackendView.as_view({'get': 'list'})),
    path('looking-for/', GetLookingForView.as_view({'get': 'list'})),
    path('developer/', GetDeveloperView.as_view({'get': 'list'})),
    path('devops/', GetDevOpsView.as_view({'get': 'list'})),
    path('pm/', GetPMView.as_view({'get': 'list'})),
    path('designer/', GetDesignerView.as_view({'get': 'list'})),
    path('analyst/', GetAnalystView.as_view({'get': 'list'})),
    path('qa/', GetQAView.as_view({'get': 'list'})),
    path('hr/', GetHRView.as_view({'get': 'list'})),
    path('ad/', GetADView.as_view({'get': 'list'})),

]