from django.db import models
from django.db.models import Model
from django.db.models.fields import URLField, DateTimeField, TextField
from django.db.models import Model
from django.db.models.fields import URLField, DateTimeField, TextField, CharField
from django.db.models.fields.related import ForeignKey
from django.db.utils import IntegrityError

class TipoProducto(Model):
    nombre = CharField(max_length=1000, null=False, blank=False, db_index=True, primary_key=True)
    descripcion = TextField()

    def __str__(self):
        return str(self.nombre)


class Producto(Model):
    tipo = ForeignKey(TipoProducto, on_delete=models.DO_NOTHING, related_name='productos')
    nombre = CharField(max_length=1000, null=False, blank=False, db_index=True, primary_key=True)
    descripcion = TextField()

    def __str__(self):
        return str(self.nombre)