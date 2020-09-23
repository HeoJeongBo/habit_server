from rest_framework import serializers
from habit_category.models import HabitCategory
from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    habit_category = serializers.SlugRelatedField(
        queryset=HabitCategory.objects.all(), slug_field='category_name',)

    class Meta:
        model = Habit
        fields = (
            'category',
            'due_date',
            'name',
            'actor',
        )
