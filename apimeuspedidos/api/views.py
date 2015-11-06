from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Pedido, ItemPedido
from .serializers import PedidoSerializer, ItemPedidoSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'PUT', 'POST'])
@csrf_exempt
def pedido(request):
    """Lista com todos os pedidos ou cria um novo pedido."""
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PedidoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'POST'])
@csrf_exempt
def item_pedido(request):
    """Lista com todos os item_pedido ou cria um novo item_pedido."""
    if request.method == 'GET':
        item = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(item, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemPedidoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def pedido_detail(request, pk):
    """Retrieve, update ou deleta um pedido."""
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PedidoSerializer(pedido, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pedido.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def item_pedido_detail(request, pk):
    """Retrieve, update ou deleta um item_pedido."""
    try:
        item = ItemPedido.objects.get(pk=pk)
    except ItemPedido.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemPedidoSerializer(item)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemPedidoSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
