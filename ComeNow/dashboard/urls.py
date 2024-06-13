from django.urls import path
from . import views

urlpatterns = [
    path("event-list/", views.eventList, name="event-list"),
    path("update-event/<int:event_id>/", views.updateEvent, name="update-event"),
    
    path("user-list/", views.userList, name="user-list"),
]
