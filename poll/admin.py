from django.contrib import admin

from poll.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'time_of_creations']
    search_fields = ['question']
    fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'variant_text', 'poll']
    search_fields = ['question']
    fields = ['variant_text']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer)
