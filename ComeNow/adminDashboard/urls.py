from django.urls import path
from . import views

urlpatterns = [
    path("admin-dashboard/", views.adminDashboard, name="admin-dashboard"),
    
    # User Management
    path("user-list/", views.UserList, name="user-list"),
    path("update-user/<int:id>/", views.UpdateUser, name="update-user"),
    path("user-delete/<int:id>/", views.DeleteUser, name="delete-user"),
    
    # Event Management
    path("event-list/", views.EventList, name="event-list"),
    path("create-event/", views.CreateEvent, name="create-event"),
    path("update-page/<int:id>/", views.updateEvent, name="update-event"),
    path("delete-event/<int:id>/", views.deleteEvent, name='delete-event'),
]
