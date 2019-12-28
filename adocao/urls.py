from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', AdocaoView.as_view(), name='adocao'),
    path('cadastrar/', CadastroAdocaoView.as_view(), name='cadastrar_adocao'),
    path('editar/<int:pk>', EditarAdocaoView.as_view(), name='editar_adocao'),
    path('excluir/<int:pk>', ExcluirAdocaoView.as_view(), name='excluir_adocao'),

]