from rest_framework_json_api import serializers
from driver_api.models import Driver, Vehicle


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('first_name', 'last_name', 'created_at', 'updated_at')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'with_drivers', 'plate_number', 'created_at', 'updated_at')


