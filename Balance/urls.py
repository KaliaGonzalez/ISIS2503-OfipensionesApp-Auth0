from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('balances/', views.balance_list),
    path('balancecreate/', csrf_exempt(views.create_balance), name='balanceCreate'),
]