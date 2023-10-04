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