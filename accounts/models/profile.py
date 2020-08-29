from django.db import models
from django.contrib.auth.models import User
from rules.contrib.models import RulesModelBase, RulesModelMixin


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
