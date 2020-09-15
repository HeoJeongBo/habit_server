from rest_framework import serializers
from habit_category.models import HabitCategory

# @detail_route -> 단일, @list_route -> 리스트


class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = '__all__'
