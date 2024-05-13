from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.view_student, name="view_student"),
    path("add", views.add, name="add"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
]