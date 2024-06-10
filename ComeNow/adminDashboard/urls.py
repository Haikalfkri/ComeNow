from django.urls import path
from . import views

urlpatterns = [
    path("admin-dashboard/", views.adminDashboard, name="admin-dashboard"),
    path("event-list/", views.EventList, name="event-list"),
    path("create-event/", views.CreateEvent, name="create-event"),
    path("update-page/<int:id>/", views.updateEvent, name="update-event"),
]
