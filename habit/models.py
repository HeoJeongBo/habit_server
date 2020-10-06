from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

# Create your models here.


class Habit(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="habits"
    )
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    check_day_of_week = ArrayField(models.BooleanField(default=False), size=7,)

    def __str__(self):
        return self.name
