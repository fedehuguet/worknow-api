from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from accounts.urls import router as account_router

router = routers.DefaultRouter()
router.registry.extend(account_router.registry)

urlpatterns = [
    # Django admin, auth and docs routes
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include(router.urls)),
]
