from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from payment.models import Payment
from payment.serializers import ListUserPaymentSerializers, AddPaymentSerializers
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class PaymentViewSet(viewsets.ViewSet):

    queryset = User.objects.all()
    serializer_class = ListUserPaymentSerializers
    # permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = ListUserPaymentSerializers(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60))
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ListUserPaymentSerializers(user)
        return Response(serializer.data)


class AddPaymentViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin):

    queryset = Payment.objects.all()
    serializer_class = AddPaymentSerializers