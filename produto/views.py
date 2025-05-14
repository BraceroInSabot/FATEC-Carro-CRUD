from django.shortcuts import render
from django.views.generic import ListView, UpdateView
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
        
class EditarProdutoView(UpdateView):
    template_name = "editar.html"

    def get_queryset(self, id: int):
        try:
            return Carro.objects.get(codigoCarro=id)
        except Carro.DoesNotExist:
            return False
    
    def get(self, request, *args, **kwargs):
        codigo = kwargs.get("pk")
        try:
            carro = self.get_queryset(codigo)
            if not carro:
                return HttpResponse(status=404, content="Carro não encontrado.")
            return render(request, self.template_name, {"carro": carro})
        except Carro.DoesNotExist:
            return HttpResponse(status=404, content="Carro não encontrado.")
        
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get("pk")
        modelo = request.POST.get("modelo")
        marca = request.POST.get("marca")
        ano = request.POST.get("ano")
        cor = request.POST.get("cor")
        dataEntrada = request.POST.get("dataEntrada")
        combustivel = request.POST.get("combustivel")
        
        try:
            carro = self.get_queryset(codigo)
            if not carro:
                return HttpResponse(status=404, content="Carro não encontrado.")
            carro.modelo = modelo
            carro.marca = marca
            carro.ano = ano
            carro.cor = cor
            carro.dataEntrada = dataEntrada
            carro.combustivel = combustivel
            carro.save()
            return HttpResponse(status=200, content="Carro editado com sucesso.")
        except Exception as e:
            return HttpResponse(status=400, content=f"Erro ao editar carro: {e}")
