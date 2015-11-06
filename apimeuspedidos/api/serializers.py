from rest_framework import serializers
from .models import Pedido, ItemPedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'cliente',)


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ('id', 'nome', 'preco', 'quantidade', 'pedido')
