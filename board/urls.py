from django.conf.urls import url, include
from board.views import board_list, board_detail, BoardAPIView, BoardDetail, GenericAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^test', GenericAPIView)

app_name = 'board'

urlpatterns = [
    # url(r'board/$', board_list),
    # url(r'^board/(?P<pk>[0-9]+)/$', board_detail)
    url(r'^board/$', BoardAPIView.as_view()),
    url(r'^board/(?P<id>[0-9]+)/$', BoardDetail.as_view()),
    url(r'^', include(router.urls))
    # url(r'^generic/board/(?P<id>[0-9]+)', GenericAPIView.as_view())
]
