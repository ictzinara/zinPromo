"""zinPromo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import index, vrn_eligibility, apply, provincial_winners, upload

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('Api.urls')),
    path('', index, name='index'),
    path('vrn_eligibility', vrn_eligibility, name='vrn_eligibility'),
    path('apply', apply, name='apply'),
    path('weekly_draw', provincial_winners, name='weekly_draw'),
    path('upload', upload, name='upload'),
]
