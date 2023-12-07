from rest_framework import permissions, viewsets

from core.models import Swimlane
from core.serializers import SwimlaneSerializer


class SwimlaneViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SwimlaneSerializer
    queryset = Swimlane.objects.all().order_by("pk")
