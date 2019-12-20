from django.shortcuts import render
from .forms import PedidoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastro(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Pedido realizado com sucesso"
        }
        return render(request, 'form.html', context)
    context = {
        'formulario':form
    }
    return render(request, 'form.html', context)