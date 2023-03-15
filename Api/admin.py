from django.contrib import admin

from Api.models import City, Province, GrandPriceDraw, PromotionWeeklyDraw, PromotionApplicant, LicenseDb

# Register your models here.
admin.site.register(LicenseDb)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(PromotionApplicant)
admin.site.register(PromotionWeeklyDraw)
admin.site.register(GrandPriceDraw)
