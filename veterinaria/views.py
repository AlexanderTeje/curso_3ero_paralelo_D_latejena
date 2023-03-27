from django.db.models import Q
from django.shortcuts import render, redirect
from veterinaria.models import duenomascota,animal#proveedor,producto
from django.contrib import messages
# Create your views here.
def home(request):
    proveedores = duenomascota.objects.all()
    messages.success(request, '¡Dueños listados!')
    productos = animal.objects.all()
    messages.success(request, '¡Animales listados!')
    return render(request, "gestion.html", {"proveedores":proveedores,
                                                    "productos": productos
                                                    })
def registroproveedor(request):
    proveid= request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proovedores = duenomascota.objects.create(id=proveid,
                                           nombre=provenom,
                                           direccion=provedire,
                                           telefono=provetelef)
    messages.success(request, '¡Dueños listados!')
    return redirect('gestion_producto')

def registroproducto(request):
    producid= request.POST['txtidpro']
    producnombre= request.POST['txtNombrepro']
    producdescri= request.POST['txtdescrippro']
    proveeid = request.POST['txtidproovee']
    productos = animal.objects.create(id=producid,
                                          nombre=producnombre,
                                          descripcion_consulta=producdescri,
                                        dueno_id=proveeid)
    messages.success(request, '¡Animal Registrado!')
    return redirect('gestion_producto')


def eliminarproveedor(request,id):
    proves = duenomascota.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Dueño Eliminado!')
    return redirect('gestion_producto')

def eliminarproducto(request,id):
    proves = animal.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Mascota Eliminado!')
    return redirect('gestion_producto')

def editarproveedor(request,id):
    proves = duenomascota.objects.get(id=id)
    return render(request,"edicioncliente.html",{"editprove":proves})

def guardaredicioproveedor(request):
    proveid = request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proves = duenomascota.objects.get(id=proveid)
    proves.nombre = provenom
    proves.direccion = provedire
    proves.telefono = provetelef
    proves.save()
    messages.success(request, '¡Dueño Actualizados!')

    return redirect('gestion_producto')

def editarproducto(request,id):
    producs = animal.objects.get(id=id)
    return render(request,"edicionmascota.html",{"editproduc":producs})

def guardaredicioproducto(request):
    produid = request.POST['txtidpro']
    produnom= request.POST['txtNombrepro']
    produdesc= request.POST['txtdescrippro']


    produc = animal.objects.get(id=produid)
    produc.nombre = produnom
    produc.descripcion_consulta = produdesc
    produc.save()
    messages.success(request, '¡Mascota Actualizado!')

    return redirect('gestion_producto')