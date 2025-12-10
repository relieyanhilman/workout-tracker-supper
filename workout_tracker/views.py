from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Exercise, ExerciseCategory, ExerciseMuscleGroup, MuscleGroup


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


def post_exercise(request):
    try:
        selected_category = request.POST["category"]
        selected_muscle_group = request.POST.getlist("muscle_group")
        exercise_name = request.POST["exercise_name"]

        # cari category string ini ada di ID berapa
        id_category = ExerciseCategory.objects.get(category_name=selected_category).id

        # cari muscle group ini ada di ID berapa
        id_muscle_group = []
        for item in selected_muscle_group:
            id_muscle_group.append(MuscleGroup.objects.get(muscle_group_name=item).id)

    except (KeyError, ExerciseCategory.DoesNotExist, MuscleGroup.DoesNotExist):
        return render(
            request,
            "workout_tracker/exercise_post.html",
            {"error_message": "Post exercise failed, please try again!"},
        )

    else:
        # Membuat object Exercise dan post ke db
        new_exercise = Exercise(
            exercise_name=exercise_name,
            exercise_category=ExerciseCategory.objects.get(id=id_category),
        )
        new_exercise.save()

        # Membuat object ExerciseMuscleGroup dan post ke db
        for id_mg in id_muscle_group:
            new_exercise_muscle_group = ExerciseMuscleGroup(
                exercise=new_exercise, muscle_group=MuscleGroup.objects.get(id=id_mg)
            )
            new_exercise_muscle_group.save()

        return render(
            request,
            "workout_tracker/exercise_post.html",
            {"message": "Post exercise success!"},
        )
