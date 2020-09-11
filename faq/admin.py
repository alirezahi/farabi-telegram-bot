from django.contrib import admin
from .models import QuestionSet, Config

# Register your models here.

class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'active', 'rank')
    fields = ('question', 'answer', 'active')
    readonly_fields = ('rank', )


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(Config, ConfigAdmin)