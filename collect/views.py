from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.db.models import Count, OuterRef, Sum
from django.contrib.auth.models import User

from payment.models import Payment
from collect.models import Collect

from collect.serializers import CollectSerializer


class CollectViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin):

    serializer_class = CollectSerializer

    def get_queryset(self):

        queryset = Collect.objects.all().annotate(
            donated_count=Sum(
                Payment.objects.filter(
                    pay_for_collect=OuterRef('id')
                ).values('pay_amount')
            ),
        )

        return queryset
