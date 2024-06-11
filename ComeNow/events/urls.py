from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventView, name="events"),
    path("like/<int:event_id>/", views.like, name="event-like"),
    path("detail/<int:id>/", views.DetailPage, name="detail-page"),
]
