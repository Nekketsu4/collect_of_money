from django.urls import path, include
from rest_framework import routers
from payment.views import *


router = routers.SimpleRouter()
router.register('payments', PaymentViewSet, 'payments')
router.register('add_payments', AddPaymentViewSet, 'add_payment')


urlpatterns = [
    path('', include(router.urls)),
    # path('payments/', UserViewSet.as_view({'get': 'list'})),
    # path('payments/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'})),
]
