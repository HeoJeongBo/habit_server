from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from habit.models import Habit
from habit.serializers import HabitSerializer

#
from account.models import User

# Create your views here.


class HabitViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
