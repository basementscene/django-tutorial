from django.urls import path
# Import from the current directory
from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("", views.home, name="index")
]