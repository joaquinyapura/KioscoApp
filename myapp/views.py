from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CrearCliente
from .models import Cliente


# Create your views here.
def hello(request):
    return render(request, 'index.html')


def productos(request):
    return HttpResponse('productos')


def nuevo_cliente(request):
    if request.method == 'GET':
        return render(request, 'nuevocliente.html', {
            'form': CrearCliente()
        })
    else:
        print(request.POST)
        Cliente.objects.create(
            nombre=request.POST['nombre'], importe=request.POST['importe'])
        return redirect('/productos/')
