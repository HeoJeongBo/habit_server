from django.conf.urls import url
from account.views import registration_view, login_by_email

urlpatterns = [
    url(r'^user/register/$', registration_view),
    url(r'^user/login/$', login_by_email)
]
