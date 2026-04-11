from django.urls import path
from .views import *

urlpatterns = [

    path('credits/',CreditBalanceView.as_view(),name="user-credits"),
    path('history/',UsageLogView.as_view(),name="usage_history")

]