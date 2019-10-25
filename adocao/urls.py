from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', adocao, name='adocao'),
    path('cadastrar/', cadastrar_adocao, name='cadastrar_adocao'),
    path('editar/<int:id>', editar_adocao, name='editar_adocao'),
    path('excluir/<int:id>', excluir_adocao, name='excluir_adocao'),

]