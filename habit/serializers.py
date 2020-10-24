from rest_framework import serializers
from habit.models import Habit
from account.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def validate(self, data):
        if self.instance:
            start_date = data.get('start_date', self.instance.start_date)
            end_date = data.get('end_date', self.instance.end_date)
        else:
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            if start_date is None or end_date is None:
                raise serializers.ValidationError(
                    "start, end date is required")
        if start_date > end_date:
            raise serializers.ValidationError(
                "Start date should be before end date")
        return data

    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'user',
            'start_date',
            'end_date',
            'check_day_of_week',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        habit = Habit.objects.create(**validated_data, user=request.user)
        return habit
