from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers
from Api.views import *
from zinPromo.views import index
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ZINARA API')

router = routers.DefaultRouter()
router.register(r'weekly_draw', PromotionWeeklyDrawViewSet)
router.register(r'licenceDb', LicenseDbViewSet)


urlpatterns = [
    path('rest', include(router.urls)),
    path(r'swagger', schema_view)
]
