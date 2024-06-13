from django.urls import path
from . import views

urlpatterns = [
    path("event-list/", views.eventList, name="event-list"),
    path("update-event/<int:event_id>/", views.updateEvent, name="update-event"),
    path("delete-event/<int:event_id>/", views.deleteEvent, name="delete-event"),
    
    path("user-list/", views.userList, name="user-list"),
]
