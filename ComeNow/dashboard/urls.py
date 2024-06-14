from django.urls import path
from . import views

urlpatterns = [
    path("event-list/", views.eventList, name="event-list"),
    path("create-event/", views.createEvent, name="create-event"),
    path("update-event/<int:event_id>/", views.updateEvent, name="update-event"),
    path("delete-event/<int:event_id>/", views.deleteEvent, name="delete-event"),
    
    
    path("user-list/", views.userList, name="user-list"),
    path("create-user", views.createUser, name="create-user"),
    path("update-user/<int:user_id>/", views.userUpdate, name="update-user"),
    path("delete-user/<int:user_id>/", views.deleteUser, name='delete-user'),
]
