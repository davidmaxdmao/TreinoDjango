from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Adocao
from .forms import AdocaoForm


# Create your views here.

class AdocaoView(ListView):
    model = Adocao
    template_name = 'adocao_home.html'


class CadastroAdocaoView(CreateView):
    model = Adocao
    form_class = AdocaoForm
    template_name = 'cadastrar_adocao.html'
    success_url = reverse_lazy('adocao')


class EditarAdocaoView(UpdateView):
    model = Adocao
    form_class = AdocaoForm
    template_name = 'cadastrar_adocao.html'
    success_url = reverse_lazy('adocao')


class ExcluirAdocaoView(DeleteView):
    model = Adocao
    form_class = AdocaoForm
    template_name = 'confirmar_exclusao_adocao.html'
    success_url = reverse_lazy('adocao')

