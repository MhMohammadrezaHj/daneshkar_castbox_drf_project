# Generated by Django 5.0.4 on 2024-04-11 01:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_episode_cover'),
        ('logs', '0002_remove_seenchannels_customer_and_more'),
        ('profiles', '0003_alter_channel_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeenChannels',
            new_name='SeenChannel',
        ),
        migrations.RenameModel(
            old_name='SeenEpisodes',
            new_name='SeenEpisode',
        ),
    ]
