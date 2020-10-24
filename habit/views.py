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

from utils.parsing_datetime import parsing_time_from_str


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

    # 추후에 이 기능에 여러가지 붙일 예정
    @action(detail=False, methods=['GET'])
    def search(self, request):
        user = request.user

        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)

        dateTimeStartDate = parsing_time_from_str(start_date)
        dateTimeEndDate = parsing_time_from_str(end_date)

        if dateTimeEndDate == None or dateTimeStartDate == None:
            return Response({'message': 'start_date, end_date를 모두 올바르게 입력해주세요'}, status=status.HTTP_400_BAD_REQUEST)

        filter_kwargs = {}
        if(start_date is not None):
            filter_kwargs["start_date__gte"] = dateTimeStartDate
        if(end_date is not None):
            filter_kwargs["end_date__lte"] = dateTimeEndDate

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
