from django.contrib import admin

from .models.audiochat import AudioChat
from .models.textchat import TextChat

# Register your models here.
admin.site.register(TextChat)
admin.site.register(AudioChat)