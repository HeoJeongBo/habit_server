from django.db import models
from habit_category.models import HabitCategory
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.


class Habit(models.Model):
    habit_category = models.ForeignKey(
        HabitCategory, related_name='habits', on_delete=models.CASCADE)
    due_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    actor = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
