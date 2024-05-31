from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventView, name="events"),
    path("detail/<int:id>/", views.DetailPage, name="detail-page"),
]
