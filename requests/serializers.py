from rest_framework import serializers

from .models import (
    BasicInformation
)


class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = '__all__'
