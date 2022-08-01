from django.db import models


class Channels(models.Model):
    channel = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channels'


class Participant(models.Model):
    id_participant = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    user_name = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    is_bot = models.BooleanField(blank=True, null=True)
    channel = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participant'


class TelegramChannelsProfessions(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telegram_channels_professions'
