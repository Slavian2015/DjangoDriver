from driver_api.models import Driver, Vehicle
from driver_api.serializers import DriverSerializer, VehicleSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response


class DriverViewSet(viewsets.ModelViewSet):

    queryset = Driver.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = DriverSerializer
    filter_fields = {'created_at': ('gte', 'lte')}


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = VehicleSerializer

    filter_fields = (
        'with_drivers',
    )

    @action(detail=True, methods=["post"])
    def set_driver(self, request, pk=None):

        vehicle = self.get_object()
        if vehicle.with_drivers == 'yes':
            vehicle.with_drivers = 'no'
        else:
            vehicle.with_drivers = 'yes'
        vehicle.save()

        print(f"vehicle : {vehicle.with_drivers}")
        return Response({'status': 'driver set'})


