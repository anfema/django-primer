from django.urls import include, path
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r"tickets", views.TicketViewSet)
router.register(r"assignments", views.TicketAssignmentViewSet)
router.register(r"comments", views.TicketCommentViewSet)
router.register(r"lanes", views.SwimlaneViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
