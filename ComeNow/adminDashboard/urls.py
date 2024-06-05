from django.urls import path
from . import views

urlpatterns = [
    path("admin-dashboard/", views.adminDashboard, name="admin-dashboard")
]
