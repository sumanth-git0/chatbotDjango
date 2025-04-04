from django.db import models


class AudioChat(models.Model):
    # ROLE_CHOICES = [{role:role} for role in ['USER','ASSISTANT']]
    user_audio = models.CharField(max_length=500,null=True)  #audio_file_path
    language = models.CharField(max_length=50,null=True)
    assistant_audio = models.CharField(max_length=500,null=True)  #audio_file_path
    # role = models.CharField(
    #     max_length=10,
    #     choices=ROLE_CHOICES,
    #     default='ASSISTANT'
    # )