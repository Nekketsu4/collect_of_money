from rest_framework import viewsets, mixins
from django.db.models import Count, OuterRef, Sum, Subquery
from django.core.cache import cache

from payment.models import Payment
from collect.models import Collect

from collect.serializers import CollectSerializer


class CollectViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):

    """Сбор денежных средств"""

    serializer_class = CollectSerializer

    def get_queryset(self):

        get_cache_collect = 'cache_collect'
        cache_collect = cache.get(get_cache_collect)

        if cache_collect:
            queryset = cache_collect
        else:
            queryset = Collect.objects.all().annotate(
                donated_sum=Subquery(
                    Payment.objects.filter(
                        collect=OuterRef('pk')
                    ).values('collect__pk')
                    .annotate(res=Sum('pay_amount')).values('res'),
                    donated_count=Subquery(
                        Payment.objects.filter(
                            collect=OuterRef('pk')).values('collect__pk')
                        .annotate(res=Count('owner')).values('res'),
                    )
                )
            )
            cache.set(get_cache_collect, queryset, 20)

        return queryset
