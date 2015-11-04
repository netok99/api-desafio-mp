from django.conf.urls import url, include, patterns
from rest_framework import routers
from api import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# router = routers.DefaultRouter()
# router.register(r'^itempedido/$', views.item_pedido)
# router.register(r'^itempedido/(?P<pk>[0-9]+)/$', views.item_pedido_detail)
# router.register(r'pedido/$', views.pedido)
# router.register(r'^pedido/(?P<pk>[0-9]+)/$', views.pedido_detail)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'apimeuspedidos.views.home', name='home'),
                       # url(r'^apimeuspedidos/', include('apimeuspedidos.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^pedidos/$', views.pedido),
                       url(r'^pedidos/(?P<pk>[0-9]+)/$', views.pedido_detail),
                       url(r'^itenspedidos/$', views.item_pedido),
                       url(r'^itenspedidos/(?P<pk>[0-9]+)/$', views.item_pedido_detail),
                       # url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                       )
