from django.contrib import admin

from .models import Channels, Participant, TelegramChannelsProfessions

admin.site.register(Channels)
admin.site.register(Participant)
admin.site.register(TelegramChannelsProfessions)
