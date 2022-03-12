from dataclasses import field
from rest_framework import serializers
from firstRevise.models import Registration

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields='__all__'