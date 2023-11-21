from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import TipoProducto, Producto
from .serializers import TipoProductoSerializer,ProductoSerializer
from rest_framework.decorators import action
from django.db.models.aggregates import Count


class TipoProductoViewSet(ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
