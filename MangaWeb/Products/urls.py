from django.test import TestCase

# Create your tests here.
from django.urls import path, re_path, include
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductoViewSet, TipoProductoViewSet

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tipos', TipoProductoViewSet)
router.register(r'producto', ProductoViewSet)

urlpatterns = router.urls
"""
urlpatterns = [

    path('tipos/', TipoProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='tipos'),
    path('productos/', ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='productos'),
]"""