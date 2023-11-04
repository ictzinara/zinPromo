from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User


class PromotionWeeklyDrawViewSet(viewsets.ModelViewSet):
    queryset = PromotionWeeklyDraw.objects.all().order_by('id')
    serializer_class = PromotionWeeklyDrawSerializer


class LicenseDbViewSet(viewsets.ModelViewSet):
    queryset = LicenseDb.objects.all().order_by('id')
    serializer_class = LicenseDbSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Define the VehicleViewSet class with the queryset and serializer_class attributes
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleSerializer


# Define the TariffViewSet class with the queryset and serializer_class attributes
class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class VehicleDetailView(generics.RetrieveAPIView):
    queryset = LicenseDb.objects.all()
    serializer_class = LicenseDbSerializer
    lookup_field = 'REGISTRATION_NO'
    

# Vehicle viewset
class VehicleViewSet(viewsets.ModelViewSet):
    # Queryset
    queryset = Vehicle.objects.all()
    # Serializer class
    serializer_class = VehicleSerializer
    
# KYC viewset
class KYCViewSet(viewsets.ModelViewSet):
    # Queryset
    queryset = KYC.objects.all()
    # Serializer class
    serializer_class = KYCSerializer

# Vehicle owner viewset
class VehicleOwnerViewSet(viewsets.ModelViewSet):
    # Queryset
    queryset = VehicleOwner.objects.all()
    # Serializer class
    serializer_class = VehicleOwnerSerializer

# Vehicle current user viewset
class VehicleCurrentUserViewSet(viewsets.ModelViewSet):
     # Queryset
     queryset = VehicleCurrentUser.objects.all()
     # Serializer class
     serializer_class = VehicleCurrentUserSerializer

# viewsets.py
from rest_framework import viewsets
from .models import Workplace, Standard, Requirement, Indicator, Record
from .serializers import WorkplaceSerializer, StandardSerializer, RequirementSerializer, IndicatorSerializer, RecordSerializer

# A viewset for the Workplace model
class WorkplaceViewSet(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer

# A viewset for the Standard model
class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

# A viewset for the Requirement model
class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

# A viewset for the Indicator model
class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

# A viewset for the Record model
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
# viewsets.py
from rest_framework import viewsets
from .models import Workplace, Risk, Incident, Audit, Compliance
from .serializers import WorkplaceSerializer, RiskSerializer, IncidentSerializer, AuditSerializer, ComplianceSerializer

class WorkplaceViewSet(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

class ComplianceViewSet(viewsets.ModelViewSet):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

class ChecklistItemViewSet(viewsets.ModelViewSet):
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
