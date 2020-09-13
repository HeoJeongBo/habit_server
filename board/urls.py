from django.conf.urls import url
from board.views import board_list, board_detail, BoardAPIView, BoardDetail, GenericAPIView

urlpatterns = [
    # url(r'board/$', board_list),
    # url(r'^board/(?P<pk>[0-9]+)/$', board_detail)
    url(r'^board/$', BoardAPIView.as_view()),
    url(r'^board/(?P<id>[0-9]+)/$', BoardDetail.as_view()),
    url(r'^generic/board/(?P<id>[0-9]+)', GenericAPIView.as_view())
]
