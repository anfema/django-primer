from django.contrib import admin

from core.models import TicketAssigment


@admin.register(TicketAssigment)
class TicketAssignmentAdmin(admin.ModelAdmin):
    list_display = ["ticket_id", "assigned_to"]
    list_filter = ["assigned_to"]
    search_fields = ["assigned_to__username"]
