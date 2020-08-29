from workouts.models import Exercise, WorkoutPlan, Workout
from workouts.serializers import ExerciseSerializer, WorkoutSerializer, WorkoutPlanSerializer
from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
