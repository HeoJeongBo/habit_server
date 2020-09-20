from django.conf.urls import url, include
from rest_framework import routers

from habit_category.views import HabitCategoryViewSet

router = routers.DefaultRouter()
router.register(r'^habit_category', HabitCategoryViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
