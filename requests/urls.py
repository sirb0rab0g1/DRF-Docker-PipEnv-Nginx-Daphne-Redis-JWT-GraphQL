from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views as jwt_views

from graphene_django.views import GraphQLView

from requests.schema import schema

from .views import (
    LoginViewSet,
    SignupViewSet,
)

from . import views

router = DefaultRouter()
router.register(r'information', views.UserProfileViewSet)

urlpatterns = [
    path('graphiql', GraphQLView.as_view(graphiql=True, schema=schema)), # view for graphql
    path('sign-in/', LoginViewSet.as_view(), name='sign-in'),  # making private view
    path('sign-up/', SignupViewSet.as_view(), name='sign-up'),
    path('api-token-auth/', jwt_views.obtain_jwt_token),
    path('api-token-refresh/', jwt_views.refresh_jwt_token),
    path('api-token-verify/', jwt_views.verify_jwt_token),
    path('', include(router.urls)),
]
