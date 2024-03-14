from rest_framework import serializers
from collect.models import Collect
from payment.models import Payment


class PaymentInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='owner.first_name')
    last_name = serializers.CharField(source='owner.last_name')

    class Meta:
        model = Payment
        fields = ['first_name', 'last_name', 'pay_amount', 'date_pay']


class CollectSerializer(serializers.ModelSerializer):

    donated_sum = serializers.IntegerField(read_only=True)
    donated_count = serializers.IntegerField(read_only=True)
    payments = PaymentInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Collect
        fields = [
            'author_collect', 'title',
            'reason', 'description',
            'goal_collect', 'donated_sum',
            'donated_count', 'img_collect',
            'last_day_collect', 'payments'
        ]