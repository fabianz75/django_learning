from django.urls import path
from cuav import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vendors", views.display_vendors, name="display_vendors"),
    path("device_count", views.display_device_count, name="display_device_count")
]