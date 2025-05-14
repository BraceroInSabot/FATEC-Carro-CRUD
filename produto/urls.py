from django.urls import path
from .views import ListarProdutoView, EditarProdutoView, DeletarProdutoView

urlpatterns = [
    path("listar/", ListarProdutoView.as_view(), name="listar_produto"),
    path("editar/<int:pk>", EditarProdutoView.as_view(), name="editar_produto"),
    path("deletar/<int:pk>", DeletarProdutoView.as_view(), name="deletar_produto"),
]