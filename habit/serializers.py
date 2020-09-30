from rest_framework import serializers
from habit.models import Habit
from account.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = (
            'due_date',
            'name',
            'user',
            'start_date',
            'end_date',
            'check_day_of_week',
        )

    def __str__(self):
        return self.name

    # validation
    def validate(self, data):
        print("In Habit Validation")
        if self.instance:
            print("update")
            pass
        else:
            print('create')
            pass
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        habit = Habit.objects.create(**validated_data, user=request.user)
        return habit
