# Generated by Django 5.0.4 on 2024-04-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activites', '0004_remove_comment_customer_remove_like_customer_and_more'),
        ('logs', '0002_remove_seenchannels_customer_and_more'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
