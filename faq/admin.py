from django.contrib import admin
from .models import QuestionSet

# Register your models here.

class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'active', 'rank')
    fields = ('question', 'answer', 'active')
    readonly_fields = ('rank', )

admin.site.register(QuestionSet, QuestionSetAdmin)