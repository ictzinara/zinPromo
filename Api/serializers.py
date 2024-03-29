from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']
class PromotionWeeklyDrawSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PromotionWeeklyDraw
        fields = (
            'id', 'weekly_winner',
        )


class LicenseDbSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = LicenseDb
        fields = (
            'id',
            'EXPIRED',
            'REGISTRATION_NO',
            'LICENSE_STATUS',
            'PENALTY_AMOUNT',
            'ARREAR_AMOUNT',
            'LAST_LICENSING_TRANSACTION',
            'BLACKLISTED',
            'LICENCE_EXPIRY_DATE',
            'Date_Captured'
        )


# Define the VehicleSerializer class with the fields id, vehicle_class and vehicle_mass
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleClass
        fields = ['id', 'vehicle_class', 'vehicle_mass']

# Define the TariffSerializer class with the fields id, fee_type, amount and vehicle (nested serializer)
class TariffSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    class Meta:
        model = Tariff
        fields = ['id', 'fee_type', 'amount', 'vehicle']

