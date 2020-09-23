from django.conf.urls import url, include
from rest_framework import routers
from habit.views import HabitViewSet

router = routers.DefaultRouter()
router.register(r'^habit', HabitViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
