from . import views
from django.urls import path

urlpatterns = [
    path ('', views.index, name = 'lottery_index'),
    path ('get-lotteries/', views.Lotteries.as_view(), name = 'lottery_get_lotteries'),
    path ('save-tickets/', views.SaveTickets.as_view(), name = "lottery_save_tickets")
]
