from rest_framework import serializers


class CollectSerializer(serializers.Serializer):

    donated_count = serializers.IntegerField()