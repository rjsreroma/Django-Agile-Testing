from rest_framework import serializers  # type: ignore
from .models import Value, Principle


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", "title", "description"]


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ["id", "title", "description"]
