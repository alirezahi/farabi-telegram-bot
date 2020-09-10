from django.contrib import admin
from .models import QuestionSet

# Register your models here.

class QuestionSetAdmin(admin.ModelAdmin):
    fields = ('question', 'answer', 'active')
    readonly_fields = ('rank', )

admin.site.register(QuestionSet)