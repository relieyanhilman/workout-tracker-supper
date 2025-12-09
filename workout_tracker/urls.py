from django.urls import path

from . import views

app_name = "workout_tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("v1/exercises", views.list_exercises, name="exercises"),
    path(
        "v1/exercises/<int:exercise_id>/", views.detail_exercise, name="exercise_detail"
    ),
    path("v1/create_exercise", views.create_exercise, name="create_exercise"),
]
