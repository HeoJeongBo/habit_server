from django.db import models
# Create your models here.
# from habit.serializers import HabitSerializer


class HabitCategory(models.Model):
    category_name = models.CharField(max_length=100, null=False)
    is_used = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
