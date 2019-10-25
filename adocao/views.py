from django.shortcuts import render, redirect
from .models import Adocao
from .forms import AdocaoForm
from animais.forms import AnimalForm

# Create your views here.

def adocao(request):
    adocoes = Adocao.objects.all()
    return render(request, 'adocao_home.html', {'adocoes':adocoes})

def cadastrar_adocao(request):
    if request.method == 'POST':
        adocao_form = AdocaoForm(request.POST)

        if adocao_form.is_valid():

            adocao_form.save()
            return redirect('adocao')
    else:
        adocao_form = AdocaoForm()

        return render(request, 'cadastrar_adocao.html', {'adocao_form':adocao_form})

def editar_adocao(request, id):
    adocao = Adocao.objects.get(id=id)
    adocao_form = AdocaoForm(request.POST or None, instance=adocao)
    if adocao_form.is_valid():
        adocao_form.save()
        return redirect('adocao')
    return render(request,'cadastrar_adocao.html', {'adocao_form':adocao_form})

def excluir_adocao(request, id):
    adocao = Adocao.objects.get(id=id)
    if request.method == 'POST':
        adocao.delete()
        return redirect('adocao')
    return render (request,'confirmar_exclusao.html', {'adocao':adocao})

