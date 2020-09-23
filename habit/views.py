from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from habit.models import Habit
from habit.serializers import HabitSerializer

#
from account.models import User
from habit_category.models import HabitCategory

# Create your views here.


class HabitViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        email = request.data['actor']
        name = request.data['name']
        category_name = request.data['category_name']

        try:
            user = User.objects.get(email=email)
        except:
            return Response({'message': '존재하지 않는 유저입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            habit_category = HabitCategory.objects.get(
                category_name=category_name)
        except:
            return Response({'message': '존재하지 않는 습관 카테고리입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        new_habit = Habit.objects.create(
            actor=email, category=habit_category, name=name
        )
        new_habit.save()
        serializer = HabitSerializer(new_habit)

        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
