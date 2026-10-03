from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


@login_required
def lista_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'productos/lista.html',
        {'productos': productos}
    )


@login_required
def crear_producto(request):

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Producto creado correctamente.'
            )

            return redirect('lista_productos')

    else:
        formulario = ProductoForm()

    return render(
        request,
        'productos/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Crear producto'
        }
    )


@login_required
def editar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = ProductoForm(
            request.POST,
            instance=producto
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Producto actualizado correctamente.'
            )

            return redirect('lista_productos')

    else:
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'productos/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Editar producto'
        }
    )


@login_required
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()

        messages.success(
            request,
            'Producto eliminado correctamente.'
        )

        return redirect('lista_productos')

    return render(
        request,
        'productos/eliminar.html',
        {'producto': producto}
    )