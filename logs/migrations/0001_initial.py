# Generated by Django 5.0.4 on 2024-04-07 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
        ('profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeenChannels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_seens', to='profiles.channel')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_seens', to='profiles.customer')),
            ],
            options={
                'ordering': ('pk',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeenEpisodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_watched', to='profiles.customer')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode_watched', to='contents.episode')),
            ],
            options={
                'ordering': ('pk',),
                'abstract': False,
            },
        ),
    ]
