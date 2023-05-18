from . import views
from django.urls import path

urlpatterns = [
    path ('', views.index, name = 'lottery_index'),
    path ('get-lotteries', views.get_lotteries, name = 'lottery_get_lotteries'),
]
