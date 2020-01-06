from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListarAnimaisView.as_view(), name='listar_animais'),
    path('cadastrar_animal/', CadastrarAnimaisView.as_view(), name='cadastrar_animal'),
    path('editar_animal/<int:pk>', EditarAnimaisView.as_view(), name='editar_animal'),
    path('remover_animal/<int:pk>', RemoverAnimalView.as_view(), name='remover_animal'),
    path('detalhe_animal/<int:pk>', DetalheAnimalView.as_view(), name='detalhe_animal'),
    path('busca_animal/', BuscaAnimalView.as_view(), name='busca_animal'),

]

