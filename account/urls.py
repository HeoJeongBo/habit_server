from django.conf.urls import url
from account.views import registration_view

urlpatterns = [
    url(r'^user/$', registration_view)
]
