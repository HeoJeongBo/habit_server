from rest_framework import serializers
from habit_category.models import HabitCategory
from habit.models import Habit


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    habit_category = serializers.SlugRelatedField(
        queryset=HabitCategory.objects.all(), slug_field=)

    class Meta:
        model = Habit
        fields = (
            'url',
            'habit_category',
            'due_date',
            'name',
            'actor',
        )
