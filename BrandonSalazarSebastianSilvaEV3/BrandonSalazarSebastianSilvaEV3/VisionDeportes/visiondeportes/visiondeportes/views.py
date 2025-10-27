from django.shortcuts import render

def paginaInicio(request):
    return render(request, 'inicio.html')
def paginaProductos(request):
    return render(request, 'productos.html')
def login(request):
    return render(request, 'login.html')
def categorias(request):
    return render(request, 'categorias.html')