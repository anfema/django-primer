from django.db import models


class Swimlane(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the swimlane", unique=True)
    description = models.TextField(blank=True, help_text="A description of the swimlane")

    def __str__(self) -> str:
        return self.name
