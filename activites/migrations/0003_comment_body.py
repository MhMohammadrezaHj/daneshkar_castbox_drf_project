# Generated by Django 5.0.4 on 2024-04-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activites', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
