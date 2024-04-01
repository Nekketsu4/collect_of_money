from rest_framework import serializers
from payment.models import Payment
from django.contrib.auth.models import User


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["pay_amount", "date_pay"]


class ListUserPaymentSerializers(serializers.ModelSerializer):
    payments = PaymentSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'payments']


class AddPaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['pay_amount', 'owner', 'date_pay', 'collect']
