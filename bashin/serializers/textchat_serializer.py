from rest_framework import serializers

from bashin.models.textchat import TextChat


class TextChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextChat
        fields = '__all__'