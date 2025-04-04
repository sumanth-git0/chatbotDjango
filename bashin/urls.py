from django.urls import path

from bashin.views.audiochat_view import AudioChatView
from bashin.views.textchat_view import TextChatView


urlpatterns = [
    path('',TextChatView.as_view(),name='text-chat'),
    path('audio', AudioChatView.as_view(), name='audio-chat'),
]