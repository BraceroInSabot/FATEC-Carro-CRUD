from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import Carro


class ListarProdutoView(ListView):
    template_name = "index.html"

    def get_queryset(self):
        try:
            return Carro.objects.all()
        except Carro.DoesNotExist:
            return HttpResponse(status=404, content="Carros não encontrados.")
    
    def get(self, request):
        try:
            carros = self.get_queryset()
            return render(request, self.template_name, {"carros": carros})
        except Carro.DoesNotExist:
            return HttpResponse(status=404, content="Carros não encontrados.")