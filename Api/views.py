from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class PromotionWeeklyDrawViewSet(viewsets.ModelViewSet):
    queryset = PromotionWeeklyDraw.objects.all().order_by('id')
    serializer_class = PromotionWeeklyDrawSerializer

class LicenseDbViewSet(viewsets.ModelViewSet):
    queryset = LicenseDb.objects.all().order_by('id')
    serializer_class = LicenseDbSerializer
