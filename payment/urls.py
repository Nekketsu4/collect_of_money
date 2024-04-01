from django.urls import path, include
from rest_framework import routers
from payment.views import *


router = routers.SimpleRouter()
router.register('payments', PaymentViewSet, 'payments')



urlpatterns = [
    path('', include(router.urls)),
]
