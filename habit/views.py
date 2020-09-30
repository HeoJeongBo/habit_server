from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from habit.models import Habit
from habit.serializers import HabitSerializer

#
from account.models import User

# Create your views here.


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    # 자신의 habits
    # update(partial)
    # searching
    #
