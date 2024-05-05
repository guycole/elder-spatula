from .models import Simple

from rest_framework import serializers


class SimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Simple
        fields = ['key', 'value']
