from rest_framework.serializers import HyperlinkedModelSerializer, Serializer,\
    ModelSerializer
from rest_framework.fields import IntegerField, URLField
from .models import TipoProducto,Producto
from rest_framework import serializers

class TipoProductoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ['nombre', 'descripcion']

class ProductoSerializer(HyperlinkedModelSerializer):
    id = IntegerField(read_only=True)
    tipo = serializers.SlugRelatedField(slug_field='nombre', queryset=TipoProducto.objects.all())
    class Meta:
        model = Producto
        fields = ['id', 'tipo','nombre', 'descripcion']
