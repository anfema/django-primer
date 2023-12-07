from django.contrib import admin

from core.models import TicketComment


@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ["ticket_id", "created_by", "created_at"]
    search_fields = ["ticket__title", "ticket__created_by__username", "created_by__username"]
    readonly_fields = ["created_at", "updated_at"]
