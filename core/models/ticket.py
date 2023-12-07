from django.db import models
from core.middleware import get_current_user
from core.models import Swimlane


def backlog_lane():
    return Swimlane.objects.get(name="Backlog")


class Ticket(models.Model):
    title = models.CharField(max_length=100, help_text="Short title")
    description = models.TextField(blank=True, help_text="A description of the ticket")
    current_lane = models.ForeignKey(Swimlane, related_name="tickets", on_delete=models.PROTECT, default=backlog_lane)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey("auth.User", on_delete=models.PROTECT, default=get_current_user)

    def __str__(self) -> str:
        return f"{self.title} #{self.pk}"
