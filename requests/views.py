from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.db import transaction
from rest_framework import (
    views,
    viewsets,
)
from .models import BasicInformation
from .serializers import (
    BasicInformationSerializer,
    LoginSerializer,
    SignupSerializer,
    UserSerializer
)
from django.contrib.auth.models import User
from api.utils import generate_jwt_token
# Create your views here.


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }

class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.add_rank(serializer.data))


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.add_rank(serializer.data))


class LoginViewSet(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, format=None):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = serializer.get_user(data['username'])
            return Response({
                'user': UserProfileSerializer(user).data,
                'token': generate_jwt_token(user)
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupViewSet(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

    @transaction.atomic
    def post(self, request, format=None):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'token': generate_jwt_token(user),
            'user': UserSerializer(user).data,
        })
