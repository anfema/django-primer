from django.db import models
from core.middleware import get_current_user


class TicketComment(models.Model):
    ticket = models.ForeignKey("core.Ticket", related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(blank=True, help_text="Comment text")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey("auth.User", on_delete=models.PROTECT, default=get_current_user)

    def __str__(self) -> str:
        return f"{self.ticket} - {self.created_by.username} at {self.created_at}"
