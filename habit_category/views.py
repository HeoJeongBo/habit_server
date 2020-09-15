from rest_framework import viewsets
from habit_category.models import HabitCategory
from habit_category.serializers import HabitCategorySerializer

# Create your views here.


class HabitCategoryViewSet(viewsets.ModelViewSet):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer
