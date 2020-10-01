from rest_framework import serializers
from habit.models import Habit
from account.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # validation
    def validate(self, data):
        if self.instance:
            print("update")
        else:
            print('create')
        return data

    class Meta:
        model = Habit
        fields = (
            'pk',
            'due_date',
            'name',
            'user',
            'start_date',
            'end_date',
            'check_day_of_week',
        )

    #  date format 관련 warning 수정
    def create(self, validated_data):
        request = self.context.get('request')
        habit = Habit.objects.create(**validated_data, user=request.user)
        return habit
