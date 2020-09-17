from rest_framework import serializers
from habit_category.models import HabitCategory
from habit.models import Habit

# @detail_route -> 단일, @list_route -> 리스트


class HabitCategorySerializer(serializers.HyperlinkedModelSerializer):

    habits = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='habit-category-detail'
    )

    class Meta:
        model = HabitCategory
        fields = (
            'pk',
            'url',
            'category_name',
            'is_used'
        )
