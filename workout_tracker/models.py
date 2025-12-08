from django.db import models


class ExerciseCategory(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    category_name = models.CharField(
        max_length=20
    )  # Ini bisa diubah jadi option antara 3 (cardio, strength, dan flexibility)


# Create your models here.
class Exercise(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exercise_name = models.CharField(max_length=100)
    exercise_category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE)


class MuscleGroup(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    muscle_group_name = models.CharField(max_length=20)


class ExerciseMuscleGroup(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
