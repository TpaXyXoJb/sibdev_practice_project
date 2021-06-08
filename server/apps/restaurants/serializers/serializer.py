from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from django.contrib.auth.models import User
from yandex_geocoder import Client
from django.conf import settings
from apps.restaurants.models.restaurant import Restaurant




class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=CurrentUserDefault()
    )

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        restaurant = Restaurant(**validated_data)
        client = Client(settings.GEO_API_KEY)
        restaurant.latitude, restaurant.longitude = client.coordinates(restaurant.address)
        restaurant.save()
        return restaurant

