from django.conf.urls import url, include
from account.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'account', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
