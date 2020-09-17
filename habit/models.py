from django.db import models
from habit_category.models import HabitCategory
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.


class Habit(models.Model):
    category = models.ForeignKey(
        HabitCategory, related_name='category', on_delete=models.CASCADE)
    due_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    actor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
