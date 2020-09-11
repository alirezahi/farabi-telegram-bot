from django.contrib import admin
from .models import QuestionSet, TelegramUser, Config, BroadcastMessage
from django.contrib.auth.models import Group, User

# Register your models here.

class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'active', 'access_count')
    fields = ('question', 'answer', 'active', 'rank')
    readonly_fields = ('access_count', )


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', )


class BroadcastMessageAdmin(admin.ModelAdmin):
    list_display = ('text', )

admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(BroadcastMessage, BroadcastMessageAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)