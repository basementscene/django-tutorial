'''
File for defining url paths
'''

from django.urls import path
# Import from the current directory
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
]
