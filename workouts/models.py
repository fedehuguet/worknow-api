from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    gif_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):

    class Intensities(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    name = models.CharField(max_length=60)
    date = models.DateField()
    intesity = models.IntegerField(choices=Intensities.choices)
    estimated_duration = models.DurationField()
    sets = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutPlanExercise')

    def __str__(self):
        return self.name

# Create your models here.
class Workout(models.Model):

    class Intensities(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    date = models.DateField()
    duration = models.DurationField()
    notes = models.CharField(max_length=120)
    perceived_intensity = models.IntegerField(choices=Intensities.choices)
    estimated_calories = models.IntegerField()
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)

class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    duration = models.DurationField()
