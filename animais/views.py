from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

# Create your views here.

def listar_animais(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais':animais})

def cadastrar_animais(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('listar_animais')
    else:
        animal_form = AnimalForm()
        return render(request, 'cadastrar_animal.html', {'animal_form':animal_form})

def editar_animais(request, id):
    animal = Animal.objects.get(id=id)
    animal_form = AnimalForm(request.POST or None, instance=animal)
    if animal_form.is_valid():
        animal_form.save()
        return redirect('listar_animais')
    return render(request, 'cadastrar_animal.html', {'animal_form':animal_form})

def remover_animal(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('listar_animais')
    return render(request, 'confirmar_exclusao.html', {'animal':animal})