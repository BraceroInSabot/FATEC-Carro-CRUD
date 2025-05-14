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
    
    def post(self, request):
        modelo = request.POST.get("modelo")
        marca = request.POST.get("marca")
        ano = request.POST.get("ano")
        cor = request.POST.get("cor")
        dataEntrada = request.POST.get("dataEntrada")
        combustivel = request.POST.get("combustivel")
        try:
            carro = Carro(
                modelo=modelo,
                marca=marca,
                ano=ano,
                cor=cor,
                dataEntrada=dataEntrada,
                combustivel=combustivel
            )
            carro.save()
            return HttpResponse(status=201, content="Carro cadastrado com sucesso.")
        except Exception as e:
            return HttpResponse(status=400, content=f"Erro ao cadastrar carro: {e}")