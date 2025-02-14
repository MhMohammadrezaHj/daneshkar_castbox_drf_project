# Generated by Django 5.0.4 on 2024-04-07 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='profiles.channel')),
            ],
            options={
                'ordering': ('pk',),
                'abstract': False,
            },
        ),
    ]
