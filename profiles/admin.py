from django.contrib import admin

from profiles.models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass
