from django.contrib import admin
from django.http.request import HttpRequest

from core.models import Swimlane, Ticket


class TicketInlineAdmin(admin.TabularInline):
    model = Ticket
    extra = 0
    readonly_fields = ["created_at"]

    def has_change_permission(self, request: HttpRequest, obj: Ticket | None) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest, obj: Ticket | None) -> bool:
        return False


@admin.register(Swimlane)
class SwimlaneAdmin(admin.ModelAdmin):
    list_display = ("name", "num_tickets")
    inlines = [TicketInlineAdmin]

    def num_tickets(self, object):
        return object.tickets.count()
