from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from habit.models import Habit
from habit.serializers import HabitSerializer
from habit.permissions import IsOwner

from account.models import User


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'modify' or self.action == 'my_habits':
            permission_classes = [IsOwner, IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_habit(self, pk):
        try:
            habit = Habit.objects.get(pk=pk)
            return habit
        except Habit.DoesNotExist:
            return None

    @action(detail=False, methods=['GET'])
    def my_habits(self, request):
        user = request.user
        my_habits = Habit.objects.filter(user=user)
        serializer = self.get_serializer(my_habits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def search(self, request):
        user = request.user

        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)

        filter_kwargs = {}
        if(start_date is not None):
            filter_kwargs["start_date__gte"] = start_date
        if(end_date is not None):
            filter_kwargs["end_date__lte"] = end_date

        try:
            habits = Habit.objects.filter(**filter_kwargs, user=user)
        except ValueError:
            habits = Habit.objects.all()

        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def modify(self, request, pk):
        habit = self.get_habit(pk)
        if habit is not None:
            if habit.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = HabitSerializer(
                habit, data=request.data, partial=True)
            if serializer.is_valid():
                modified_habit = serializer.save()
                return Response(serializer.data)
