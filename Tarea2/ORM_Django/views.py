from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DetalleFactura, Factura, Producto, models, Cliente
from .forms import FacturaForm,ClienteForm,ProductoForm,DetalleFacturaForm

def menu(request):
    return render(request, 'principal.html')

#Producto
def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Producto', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto/')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)

def listarproducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Producto', 'Acerca': 'Acerca del Blog', 'productos': producto}
    return render(request, 'listarproducto.html', opciones)


def editarproducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Producto', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    product = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=product)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto/')

    return render(request, 'producto.html', opciones)

def eliminarproducto(request, id):
    produc = Producto.objects.get(id=id)
    if request.method == 'POST':
        produc.delete()
        return redirect('/listarproducto/')
    return render(request, 'eliminarproducto.html', {'Producto': produc})

#Cliente
def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Cliente', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarcliente/')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)

def listarcliente(request):
    cliente = Cliente.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto':'Lista de Cliente', 'Acerca': 'Acerca del Blog', 'clientes': cliente}
    return render(request, 'listarcliente.html', opciones)


def editarcliente(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Cliente', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/listarcliente/')

    return render(request, 'cliente.html', opciones)

def eliminarcliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/listarcliente/')
    return render(request, 'eliminarcliente.html', {'Cliente': cliente})

#Factura
def factura(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Factura', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarfactura/')
    else:
        form = FacturaForm()
        formde = DetalleFacturaForm()
        opciones['form'] = form
        opciones['idsig'] = Factura.objects.all().order_by('-id')[0].id
        opciones['formde'] = formde


    return render(request, 'factura.html', opciones)

def listarfactura(request):
    factura = Factura.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Factura', 'Acerca': 'Acerca del Blog', 'facturas': factura}
    return render(request, 'listarfacturas.html', opciones)

def editarfactura(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Factura', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    factura = Factura.objects.get(id=id)
    detfactura = DetalleFactura.objects.filter(factura__id=id).first()
    if request.method == 'GET':
        form = FacturaForm(instance=factura)
        formde = DetalleFacturaForm(instance=detfactura)
        opciones['form'] = form
        opciones['formde'] = formde
    else:
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('/listarfactura/')

    return render(request, 'factura.html', opciones)

def eliminarfactura(request, id):
    factura = Factura.objects.get(id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('/listarfactura/')
    return render(request, 'eliminarfactura.html', {'Factura': factura})
