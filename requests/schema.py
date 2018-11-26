from graphene_django import DjangoObjectType
from .models import BasicInformation
from django.contrib.auth.models import User
import graphene

class Basic(DjangoObjectType):
    class Meta:
        model = BasicInformation

class Query(graphene.ObjectType):
    users = graphene.List(Basic)

    def resolve_users(self, info):
        return BasicInformation.objects.all()

schema = graphene.Schema(query=Query)
