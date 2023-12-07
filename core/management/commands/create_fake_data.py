import random

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, CommandError
from lorem_text import lorem

from core.models import Ticket, TicketComment, TicketAssigment, Swimlane

User = get_user_model()


def create_tickets(num: int, backlog_only: bool = False):
    users = list(User.objects.all())

    # If backlog_only is true, only create tickets in the backlog swimlane
    if backlog_only:
        swimlanes = [Swimlane.objects.get(name="Backlog")]
    else:
        swimlanes = list(Swimlane.objects.all())

    for _ in range(num):
        # Create ticket
        t = Ticket.objects.create(
            title=lorem.words(10),
            description=lorem.paragraph(),
            current_lane=random.choice(swimlanes),
            created_by=random.choice(users),
        )

        # Randomly assign people
        num_assignees = round(random.uniform(0, len(users)))
        possible_assignees = list(users)
        random.shuffle(possible_assignees)
        for j in range(num_assignees):
            t.assignments.create(assigned_to=possible_assignees[j])

        # Randomly create comments
        num_comments = int(random.uniform(0, 10))
        for j in range(num_comments):
            TicketComment.objects.create(
                ticket=t,
                comment=lorem.paragraph(),
                created_by=random.choice(users),
            )


class Command(BaseCommand):
    help = "Create fake data for testing purposes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--tickets",
            action="store",
            type=int,
            help="Number of tickets to create",
        )
        parser.add_argument("--backlog", action="store_true", help="Create tickets only in backlog", default=False)

    def handle(self, *args, **options):
        ticket_count = options.get("tickets")
        backlog_only = options.get("backlog")
        if ticket_count is None:
            raise CommandError("Please specify the number of tickets to create")

        create_tickets(ticket_count, backlog_only)
