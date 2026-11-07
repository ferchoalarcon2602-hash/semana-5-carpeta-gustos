
from django.shortcuts import render, redirect, get_object_or_404

from .models import marca, moto, resena
from .forms import MarcaForm, MotoForm, ResenaForm
from .freegames import obtener_juegos


# ==================================
# PAGINA PRINCIPAL
# ==================================

def index(request):
    return render(request, 'bmw/index.html')


# ==================================
# PAGINA DE VIDEOJUEGOS
# ==================================

def videojuegos(request):

    juegos = obtener_juegos()

    busqueda = request.GET.get('q', '').strip()

    if busqueda:
        juegos = [
            juego for juego in juegos
            if busqueda.lower() in
            juego.get('title', '').lower()
        ]

    return render(
        request,
        'bmw/videojuegos.html',
        {
            'juegos': juegos,
            'busqueda': busqueda
        }
    )


# ==================================
# CRUD DE MARCAS
# ==================================

# LISTAR MARCAS
def lista_marcas(request):

    marcas = marca.objects.all()

    return render(
        request,
        'bmw/lista_marcas.html',
        {'marcas': marcas}
    )


# CREAR MARCA
def crear_marca(request):

    if request.method == 'POST':

        formulario = MarcaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_marcas')

    else:
        formulario = MarcaForm()

    return render(
        request,
        'bmw/crear_marca.html',
        {'formulario': formulario}
    )


# EDITAR MARCA
def editar_marca(request, marca_id):

    objeto = get_object_or_404(marca, id=marca_id)

    if request.method == 'POST':

        formulario = MarcaForm(
            request.POST,
            instance=objeto
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_marcas')

    else:
        formulario = MarcaForm(instance=objeto)

    return render(
        request,
        'bmw/editar_marca.html',
        {
            'formulario': formulario,
            'marca': objeto
        }
    )


# ELIMINAR MARCA
def eliminar_marca(request, marca_id):

    objeto = get_object_or_404(marca, id=marca_id)

    if request.method == 'POST':
        objeto.delete()
        return redirect('lista_marcas')

    return render(
        request,
        'bmw/eliminar_marca.html',
        {'marca': objeto}
    )


# ==================================
# CRUD DE MOTOS
# ==================================

# LISTAR MOTOS
def lista_motos(request):

    motos = moto.objects.select_related('marca').all()

    return render(
        request,
        'bmw/lista_motos.html',
        {'motos': motos}
    )


# CREAR MOTO
def crear_moto(request):

    if request.method == 'POST':

        formulario = MotoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_motos')

    else:
        formulario = MotoForm()

    return render(
        request,
        'bmw/crear_moto.html',
        {'formulario': formulario}
    )


# EDITAR MOTO
def editar_moto(request, moto_id):

    objeto = get_object_or_404(moto, id=moto_id)

    if request.method == 'POST':

        formulario = MotoForm(
            request.POST,
            instance=objeto
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_motos')

    else:
        formulario = MotoForm(instance=objeto)

    return render(
        request,
        'bmw/editar_moto.html',
        {
            'formulario': formulario,
            'moto': objeto
        }
    )


# ELIMINAR MOTO
def eliminar_moto(request, moto_id):

    objeto = get_object_or_404(moto, id=moto_id)

    if request.method == 'POST':
        objeto.delete()
        return redirect('lista_motos')

    return render(
        request,
        'bmw/eliminar_moto.html',
        {'moto': objeto}
    )


# ==================================
# CRUD DE RESEÑAS
# ==================================

# LISTAR RESEÑAS
def lista_resenas(request):

    resenas = resena.objects.select_related('moto').all()

    return render(
        request,
        'bmw/lista_resenas.html',
        {'resenas': resenas}
    )


# CREAR RESEÑA
def crear_resena(request):

    if request.method == 'POST':

        formulario = ResenaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_resenas')

    else:
        formulario = ResenaForm()

    return render(
        request,
        'bmw/crear_resena.html',
        {'formulario': formulario}
    )


# EDITAR RESEÑA
def editar_resena(request, resena_id):

    objeto = get_object_or_404(resena, id=resena_id)

    if request.method == 'POST':

        formulario = ResenaForm(
            request.POST,
            instance=objeto
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_resenas')

    else:
        formulario = ResenaForm(instance=objeto)

    return render(
        request,
        'bmw/editar_resena.html',
        {
            'formulario': formulario,
            'resena': objeto
        }
    )


# ELIMINAR RESEÑA
def eliminar_resena(request, resena_id):

    objeto = get_object_or_404(resena, id=resena_id)

    if request.method == 'POST':
        objeto.delete()
        return redirect('lista_resenas')

    return render(
        request,
        'bmw/eliminar_resena.html',
        {'resena': objeto}
    )
