from django.db import models
from django.forms import ModelForm
from Api.models import *


class PromotionApplicantForm(ModelForm):
    class Meta:
        model = PromotionApplicant
        fields = [
            'reg_number',
            'nat_id',
            'first_name',
            'last_name',
            'gender',
            'email',
            'phone',
            'province',
            'address',
        ]


class NewVehicleForm(ModelForm):
    class Meta:
        model = vlicDb
        fields = [
            'Regno',
            'Status',
            'Penalties',
            'Arrears',
            'DateLicensed',
            'ExpiryDate',
        ]

class AddVehicleForm(ModelForm):
    class Meta:
        model = LicenseDb
        fields = [
            "EXPIRED",
            "REGISTRATION_NO",
            "LICENSE_STATUS",
            "LAST_LICENSING_TRANSACTION",
            "PENALTY_AMOUNT",
            "ARREAR_AMOUNT",
            "BLACKLISTED",
            "LICENCE_EXPIRY_DATE",
        ]
