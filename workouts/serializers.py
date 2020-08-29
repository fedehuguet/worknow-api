from models.py import .*
from rest_framework import serializers


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSerializer
        fields = "__all__"
