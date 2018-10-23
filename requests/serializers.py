from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    BasicInformation
)
from rest_framework.validators import UniqueValidator
from django.db import transaction

class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = (
            'age',
            'address',
            'contact_number'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = BasicInformationSerializer()

    class Meta:
        model = User
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'username': {'required': True, 'validators': [
                UniqueValidator(
                    queryset=User.objects.all(), lookup='iexact', message='Username already exists.'
                )
            ]},
            'email': {'required': True, 'allow_blank': False, 'validators': [
                UniqueValidator(
                    queryset=User.objects.all(), lookup='iexact', message='Email already exists.'
                )
            ]},
        }

        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        BasicInformation.objects.create(user=user, **profile_data)
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        BasicInformation.objects.filter(id=instance.profile.id).update(**profile_data)

        return instance


