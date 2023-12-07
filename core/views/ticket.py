from rest_framework import permissions, viewsets

from core.models import Ticket
from core.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all().order_by("-created_at", "-updated_at")
