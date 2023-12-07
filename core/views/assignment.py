from rest_framework import permissions, viewsets

from core.models import TicketAssigment
from core.serializers import TicketAssignmentSerializer


class TicketAssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketAssignmentSerializer
    queryset = TicketAssigment.objects.all().order_by(
        "-ticket__created_at", "-ticket__updated_at", "assigned_to__id", "pk"
    )
