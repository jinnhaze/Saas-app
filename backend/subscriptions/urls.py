from django.urls import path
from .views import *


urlpatterns = [
    path('plans/',PlanView.as_view(),name="plan_list"),
    path('my-subscription/',MySubscriptionView.as_view(),name="My_subscription"),
    path('create-order/',PaymentView.as_view(),name="create-order"),
]