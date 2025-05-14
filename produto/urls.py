from django.urls import path
from .views import ListarProdutoView

urlpatterns = [
    path("listar/", ListarProdutoView.as_view(), name="listar_produto"),
]