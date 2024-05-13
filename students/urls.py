from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.view_student, name="view_student"),
    path("add", views.add, name="add"),
]