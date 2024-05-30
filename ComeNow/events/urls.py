from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventView, name="events"),
    path("detail/", views.DetailPage, name="detail-page"),
]
