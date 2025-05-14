from django.shortcuts import render
from django.views.generic import ListView

class ListarProdutoView(ListView):
    def get(self, request):
        return render(request, "index.html")