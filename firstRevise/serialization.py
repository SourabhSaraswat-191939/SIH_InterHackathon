from dataclasses import field
from rest_framework import serializers
from firstRevise.models import Registration

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields='__all__'

class Serializationsort(serializers.ModelSerializer):
    collegeName = serializers.CharField()
    total = serializers.FloatField()
    class Meta:
        model=Registration
        fields=['collegeName','total']