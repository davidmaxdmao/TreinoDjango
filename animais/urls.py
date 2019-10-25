from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', listar_animais, name='listar_animais'),
    path('cadastrar_animal/', cadastrar_animais, name='cadastrar_animal'),
    path('editar_animal/<int:id>', editar_animais, name='editar_animal'),
    path('remover_animal/<int:id>', remover_animal, name='remover_animal'),

]