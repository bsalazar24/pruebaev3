from django.shortcuts import render,redirect,get_object_or_404
from Producto.models import Producto, Categoria
from . import forms
from django.contrib import messages

def listarCategorias(request):
    categoria = Categoria.objects.all()
    return render(request, 'producto/listarCategorias.html',{'categorias':categoria})

def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/listarProductos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        formulario = forms.crearProducto(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"post creado correctamente")
            return redirect ('Producto:listarProductos')
    else:
        formulario= forms.crearProducto()
    return render (request,'producto/crear_producto.html',{'formulario':formulario})

def crear_categoria(request):
    if request.method == 'POST':
        formulario = forms.crearCategoria(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"categoria creada correctamente")
            return redirect ('Producto:listarCategorias')
    else:
        formulario= forms.crearCategoria()
    return render (request,'producto/crear_categoria.html',{'formulario':formulario})

def productos_porCategoria(request,slug):
    categoria = get_object_or_404(Categoria, slug=slug)

    productos = Producto.objects.filter(categoria=categoria)
    return render(request,'producto/listarProductos.html', {
        'productos': productos,
        'categoria': categoria
    })