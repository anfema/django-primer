from django.contrib import admin

from core.models import Ticket, TicketAssigment, TicketComment


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


class TicketAssignmentInlineAdmin(admin.TabularInline):
    model = TicketAssigment
    extra = 1


class TicketCommentInlineAdmin(admin.TabularInline):
    model = TicketComment
    extra = 0
    readonly_fields = ["created_at"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "current_lane", "created_by", "assigned_to", "created_at")
    list_filter = (
        "current_lane",
        ("created_by__username", custom_titled_filter("created by")),
        ("assignments__assigned_to__username", custom_titled_filter("assigned to")),
    )
    search_fields = ["title", "description"]
    inlines = [TicketAssignmentInlineAdmin, TicketCommentInlineAdmin]
    readonly_fields = ["created_at", "updated_at"]
    list_display_links = ["id", "title"]

    def assigned_to(self, object):
        return ",".join([a.assigned_to.username for a in object.assignments.all()])
