from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Animal
from .forms import AnimalForm

# Create your views here.


class ListarAnimaisView(ListView):
    model = Animal
    form_class = AnimalForm
    template_name = 'index.html'


class CadastrarAnimaisView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'cadastrar_animal.html'
    success_url = reverse_lazy('listar_animais')


class EditarAnimaisView(UpdateView):
    model = Animal
    template_name = 'cadastrar_animal.html'
    form_class = AnimalForm
    success_url = '/'


class RemoverAnimalView(DeleteView):
    model = Animal
    template_name = 'confirmar_exclusao_adocao.html'
    success_url = reverse_lazy('listar_animais')
