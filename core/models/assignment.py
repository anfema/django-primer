from django.db import models


class TicketAssigment(models.Model):
    ticket = models.ForeignKey("core.Ticket", related_name="assignments", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.ticket} - {self.assigned_to.username}"

    class Meta:
        unique_together = ("ticket", "assigned_to")
