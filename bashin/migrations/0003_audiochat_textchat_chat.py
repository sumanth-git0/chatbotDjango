# Generated by Django 5.1.7 on 2025-04-03 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bashin', '0002_textchat_response_text_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_audio', models.CharField(max_length=50, null=True)),
                ('assistant_audio', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='textchat',
            name='chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bashin.audiochat'),
        ),
    ]
