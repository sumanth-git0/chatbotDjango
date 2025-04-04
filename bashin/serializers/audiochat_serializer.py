from rest_framework import serializers

from bashin.models.audiochat import AudioChat

class AudioChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioChat
        fields = '__all__'