# Generated by Django 4.2.8 on 2023-12-07 15:05

from django.db import migrations


def prefill_swimlanes(apps, schema_editor):
    Swimlane = apps.get_model("core", "Swimlane")
    Swimlane.objects.bulk_create(
        [
            Swimlane(name="Backlog", description="Backlog, tickets that have not been scheduled"),
            Swimlane(name="To Do", description="Tickets in current spring"),
            Swimlane(name="In Progress", description="Tickets that are worked on"),
            Swimlane(name="To Test", description="Tickets that are ready to be tested"),
            Swimlane(name="Done", description="Tickets that are done"),
        ]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [migrations.RunPython(prefill_swimlanes)]
