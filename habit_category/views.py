from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from habit_category.models import HabitCategory
from habit_category.serializers import HabitCategorySerializer

#
from rest_framework.decorators import action
# Create your views here.


class HabitCategoryViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    serializer_class = HabitCategorySerializer
    queryset = HabitCategory.objects.all()

    # lookup field
    lookup_fields = ['category_name']

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HabitCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        category_name = request.data['category_name']

        try:
            is_same_name_exist = HabitCategory.objects.get(
                category_name=category_name
            )
        except HabitCategory.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'message': '해당 이름의 습관 카테고리가 이미 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_by_name(self, request, *args, **kwargs):
        category_name = request.GET.get('name', None)
        try:
            habit_category = HabitCategory.objects.get(
                category_name=category_name)
        except:
            return Response({'message': '해당 이름의 습관 카테고리가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = HabitCategorySerializer(habit_category)
        return Response(serializer.data, status=status.HTTP_200_OK)
