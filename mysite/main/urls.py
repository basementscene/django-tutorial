from django.urls import path
# Import from the current directory
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home")
]
