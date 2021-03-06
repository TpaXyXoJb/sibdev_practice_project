from rest_framework import status
from rest_framework import  mixins
from rest_framework.response import Response
from rest_framework import viewsets

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet ):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

