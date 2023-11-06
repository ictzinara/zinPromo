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
class EmployeeSerializer(serializers.ModelSerializer):
    # Meta
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 6
# Vehicle serializer
class VehicleSerializer(serializers.ModelSerializer):
    # Meta
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 6

# KYC serializer
class KYCSerializer(serializers.ModelSerializer):
    # Meta
    class Meta:
        model = KYC
        fields = '__all__'
        depth = 6

# Vehicle owner serializer
class VehicleOwnerSerializer(serializers.ModelSerializer):
    # Meta
    class Meta:
        model = VehicleOwner
        fields = '__all__'
        depth = 6

# Vehicle current user serializer
class VehicleCurrentUserSerializer(serializers.ModelSerializer):
     # Meta
     class Meta:
        model = VehicleCurrentUser
        fields = '__all__'
        depth = 6

# A serializer for the Workplace model
class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'
        depth = 6

# A serializer for the Standard model
class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'
        depth = 6

# A serializer for the Requirement model
class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'
        depth = 6

# A serializer for the Indicator model
class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'
        depth = 6

# A serializer for the Record model
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        depth = 6

class RiskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Risk
        fields = '__all__'
        depth = 6

class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = '__all__'
        depth = 6

class AuditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audit
        fields = '__all__'
        depth = 6

class ComplianceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compliance
        fields = '__all__'
        depth = 6


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        depth = 6

class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = '__all__'
        depth = 6