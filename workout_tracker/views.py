from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Exercise, ExerciseMuscleGroup


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Ini adalah workout tracker")


def list_exercises(request):
    exercise_list = Exercise.objects.order_by("exercise_name")
    context = {"exercise_list": exercise_list}
    return render(request, "workout_tracker/exercise_list.html", context)


def detail_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    exercise_muscle_group = ExerciseMuscleGroup.objects.filter(exercise__id=exercise_id)
    return render(
        request,
        "workout_tracker/exercise_detail.html",
        {"exercise": exercise, "exercise_muscle_group": exercise_muscle_group},
    )


def create_exercise(request):
    return render(request, "workout_tracker/exercise_create.html")
