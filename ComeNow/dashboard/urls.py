from django.urls import path
from . import views

urlpatterns = [
    # admin dashboard
    path("event-list/", views.eventList, name="event-list"),
    path("create-event/", views.createEvent, name="create-event"),
    path("update-event/<int:event_id>/", views.updateEvent, name="update-event"),
    path("delete-event/<int:event_id>/", views.deleteEvent, name="delete-event"),
    
    path("admin-analyze/", views.adminAnalyze, name="admin-analyze"),
    
    # admin profile
    path("admin-overview/<int:id>/", views.adminOverview, name="admin-overview"),
    path("admin-profile/<int:user_id>/", views.adminProfile, name="admin-profile"),
    path("admin-change-password/", views.adminPasswordChangeView.as_view(), name="admin-password-change"),
    
    path("user-list/", views.userList, name="user-list"),
    path("create-user", views.createUser, name="create-user"),
    path("update-user/<int:user_id>/", views.userUpdate, name="update-user"),
    path("delete-user/<int:user_id>/", views.deleteUser, name='delete-user'),
    
    
    # user dashboard
    path("like-events", views.eventLike, name="like-events"),
    path("saved-events", views.eventSaved, name='saved-events'),
    
    #user profile
    path("overview/<int:id>/", views.userOverview, name="user-overview"),
    path("update-profiles/<int:user_id>/", views.userProfile, name="update-profiles"),
    path("change-password-profile/", views.PasswordsChangeView.as_view(), name="change-password-profile"),
]
