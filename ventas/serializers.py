from rest_framework import serializers
from .models import Cliente

class ClienteSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cliente
        fields=['id','dni','nombre','ruc','razon','direccion']
        #fields='_all_'