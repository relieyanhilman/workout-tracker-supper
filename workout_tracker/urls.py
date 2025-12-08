from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/exercises", views.list_exercises, name="exercises"),
    path(
        "v1/exercises/<int:exercise_id>", views.detail_exercise, name="exercise_detail"
    ),
]
