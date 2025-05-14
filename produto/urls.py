from django.urls import path
from .views import ListarProdutoView, EditarProdutoView

urlpatterns = [
    path("listar/", ListarProdutoView.as_view(), name="listar_produto"),
    path("editar/<int:pk>", EditarProdutoView.as_view(), name="editar_produto"),
]