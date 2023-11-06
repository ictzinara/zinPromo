from django.contrib import admin
from Api.models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'emailId', 'department')
    # Add any other desired configurations

@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    # Add any other desired configurations

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    # Add any other desired configurations

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard')
    # Add any other desired configurations

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'requirement')
    # Add any other desired configurations

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'workplace', 'date', 'employee')
    # Add any other desired configurations

@admin.register(RecordIndicator)
class RecordIndicatorAdmin(admin.ModelAdmin):
    list_display = ('record', 'indicator', 'value')
    # Add any other desired configurations

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('workplace', 'description', 'level')
    # Add any other desired configurations

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('workplace', 'date', 'type', 'employee', 'severity', 'status')
    # Add any other desired configurations

@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_display = ('workplace', 'type', 'requirement', 'status')
    # Add any other desired configurations

@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    # Add any other desired configurations

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('workplace', 'date', 'type', 'employee', 'score')
    # Add any other desired configurations
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('province', 'description')

@admin.register(PromotionApplicant)
class PromotionApplicantAdmin(admin.ModelAdmin):
    list_display = ('reg_number', 'nat_id', 'first_name', 'last_name', 'gender', 'email', 'phone', 'province', 'address', 'application_date')

@admin.register(PromotionWeeklyDraw)
class PromotionWeeklyDrawAdmin(admin.ModelAdmin):
    list_display = ('weekly_winner', 'draw_number', 'province', 'notified', 'notified_on', 'price_claimed')

@admin.register(GrandPriceDraw)
class GrandPriceDrawAdmin(admin.ModelAdmin):
    list_display = ('weekly_winner', 'draw_number', 'province', 'position', 'notified', 'notified_on', 'price_claimed')

@admin.register(vlicDb)
class vlicDbAdmin(admin.ModelAdmin):
    list_display = ('Regno', 'Status', 'Penalties', 'Arrears', 'DateLicensed', 'ExpiryDate', 'dateCaptured')

@admin.register(LicenseDb)
class LicenseDbAdmin(admin.ModelAdmin):
    list_display = ('EXPIRED', 'REGISTRATION_NO', 'LICENSE_STATUS', 'PENALTY_AMOUNT', 'ARREAR_AMOUNT', 'LAST_LICENSING_TRANSACTION', 'BLACKLISTED', 'LICENCE_EXPIRY_DATE', 'Date_Captured')

@admin.register(VehicleClass)
class VehicleClassAdmin(admin.ModelAdmin):
    list_display = ('vehicle_class', 'vehicle_mass')

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('fee_type', 'amount', 'vehicle')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'make', 'year', 'color', 'status', 'license_plate', 'owner', 'current_user')

@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('code', 'document_type', 'document_number', 'reg_book_document')

@admin.register(VehicleOwner)
class VehicleOwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'email', 'national_identity', 'national_identity_document_image', 'kyc')

@admin.register(VehicleCurrentUser)
class VehicleCurrentUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'email', 'kyc', 'national_identity', 'national_identity_document_image')

@admin.register(DataCollection)
class DataCollectionAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'created_on', 'updated_on')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass