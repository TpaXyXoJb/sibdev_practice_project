from rest_framework import viewsets

from apps.restaurants.models.restaurant import Restaurant
from apps.restaurants.serializers.serializer import RestaurantSerializer

from url_filter.integrations.drf import DjangoFilterBackend


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'owner', 'open_time', 'close_time', 'longitude', 'latitude')