from django.db import models


class Telegram(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=700, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    time_of_public = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scraping_telegram'


    def __str__(self):
        self.view = f'{self.time_of_public} | {self.title}'
        return self.view

class NewYork(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=700, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    time_of_public = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.chat_name

