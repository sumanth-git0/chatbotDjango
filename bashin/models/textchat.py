from django.db import models

from ..models.audiochat import AudioChat


class TextChat(models.Model):
    chat = models.ForeignKey(AudioChat, on_delete=models.CASCADE, blank=True, null=True)
    input_text = models.TextField(max_length=1000, blank=True, null=True)
    translated_text = models.TextField(max_length=1000, blank=True, null=True)
    response_text = models.TextField(max_length=1000, blank=True, null=True)
    response_text_translation = models.TextField(max_length=1000, blank=True, null=True)