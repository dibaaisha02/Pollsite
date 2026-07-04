from django.contrib import admin
from .models import Poll, Option, Vote

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'is_public', 'expires_at']
    list_filter = ['is_public', 'created_at']
    search_fields = ['title', 'description']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'poll']
    search_fields = ['text']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'option']
    list_filter = ['poll']