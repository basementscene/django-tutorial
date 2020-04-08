from django.urls import path
# Import from the current directory
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view1/", views.view_1, name="view_1"),
]