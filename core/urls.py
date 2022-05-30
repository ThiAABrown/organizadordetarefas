from django.urls import path

from .views import index, planejamento, execucao

urlpatterns = [
    path('', index, name='index'),
    path('planejamento/', planejamento, name='planejamento'),
    path('execucao/', execucao, name='execucao'),
]