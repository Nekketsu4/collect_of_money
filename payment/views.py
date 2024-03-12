from django.contrib.auth.models import User
from payment.models import Payment
from payment.serializers import PaymentSerializers, ListUserPaymentSerializers, AddPaymentSerializers
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):

    queryset = User.objects.all()
    serializer_class = ListUserPaymentSerializers
    # permission_classes = [IsAuthenticated]


class AddPaymentViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin):

    queryset = Payment.objects.all()
    serializer_class = AddPaymentSerializers