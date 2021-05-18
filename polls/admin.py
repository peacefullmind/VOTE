import datetime

from django.contrib import admin
from django.utils import timezone

from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 0
    show_change_link = True


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class UserVoteInline(admin.TabularInline):
    model = models.UserVote
    fields = ['user', 'vote_datetime']
    readonly_fields = fields
    extra = 0

@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    inlines = [UserVoteInline]
