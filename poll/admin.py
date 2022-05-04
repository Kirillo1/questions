from django.contrib import admin

from poll.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'time_of_creations']
    search_fields = ['question']
    fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
