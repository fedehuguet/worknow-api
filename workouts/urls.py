from rest_framework import routers

from workouts.viewsets import .*

router = routers.DefaultRouter()
router.register("exercises", ExerciseViewSet, basename="exercises")
router.register("workouts", WorkoutViewSet, basename="workouts")
router.register("workout_plans", WorkoutPlanViewSet, basename="workout_plans")
