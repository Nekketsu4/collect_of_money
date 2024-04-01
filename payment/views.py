from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from payment.models import Payment
from payment.serializers import ListUserPaymentSerializers, AddPaymentSerializers
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class PaymentViewSet(viewsets.ModelViewSet):
    """Операция платежа"""

    serializer_class = ListUserPaymentSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return AddPaymentSerializers

        return ListUserPaymentSerializers

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    @method_decorator(cache_page(60))
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60))
    def retrieve(self, request, pk=None, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = ListUserPaymentSerializers(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
