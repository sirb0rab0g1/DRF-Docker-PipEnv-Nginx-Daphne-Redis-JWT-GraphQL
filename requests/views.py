from rest_framework import (
    viewsets,
)
from .models import BasicInformation
from .serializers import BasicInformationSerializer
# Create your views here.


class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer
