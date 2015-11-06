from django.db import models


class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente


class ItemPedido(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(max_length=20)
    quantidade = models.IntegerField()
    pedido = models.ForeignKey(Pedido)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome