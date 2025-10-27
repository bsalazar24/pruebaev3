from django.urls import path
from Producto import views
app_name = 'Producto'

urlpatterns = [          
    path('listarCategorias/', views.listarCategorias, name='listarCategorias'),
    path('listarProductos/', views.listarProductos, name='listarProductos'),
    path('crearProducto/', views.crear_producto, name='crearProducto'),
    path('crearCategoria/', views.crear_categoria, name='crearCategoria'),
    path('categoria/<slug:slug>/', views.productos_porCategoria, name='productos_porCategoria'),
]