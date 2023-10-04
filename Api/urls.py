from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from Api.views import *
from zinPromo.views import index
from rest_framework_swagger.views import get_swagger_view
from .views import UserListView, UserDetailView
schema_view = get_swagger_view(title='ZINARA API')

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'weekly_draw', PromotionWeeklyDrawViewSet)
router.register(r'licenceDb', LicenseDbViewSet)
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'tariffs', TariffViewSet, basename='tariff')
# router = routers.DefaultRouter()
# router.register(r'users-list', UserListView, basename='user-list')
# router.register(r'users/(?P<username>\w+)/', UserDetailView, basename='user-detail')

urlpatterns = [
    path('rest/', include(router.urls)),
    re_path('^users/(?P<username>.+)/$', UserDetailView.as_view()),
    re_path('^licencing/(?P<REGISTRATION_NO>.+)/$', VehicleDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api-token-auth/', CustomAuthToken.as_view()),
    path(r'swagger', schema_view)
]
