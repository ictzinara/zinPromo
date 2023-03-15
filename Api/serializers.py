from rest_framework import serializers
from .models import *


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
