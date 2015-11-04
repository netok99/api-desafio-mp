from rest_framework import serializers
from .models import Pedido, ItemPedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('cliente',)


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ('nome', 'preco', 'quantidade', 'pedido')
