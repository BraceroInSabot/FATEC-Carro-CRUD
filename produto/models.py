from django.db import models

class Carro(models.Model):
    codigoCarro = models.SmallAutoField(max_length=10, primary_key=True, db_column="CodigoCarro", verbose_name="Código Interno")
    modelo = models.CharField(max_length=50, db_column="Modelo", verbose_name="Modelo do Carro")
    marca = models.CharField(max_length=50, db_column="Marca", verbose_name="Marca do Carro")
    ano = models.IntegerField(db_column="Ano", verbose_name="Ano do Carro")
    cor = models.CharField(max_length=20, db_column="Cor", verbose_name="Cor do Carro")
    dataEntrada = models.DateField(db_column="DataEntrada", verbose_name="Data de Entrada")
    combustivel = models.CharField(choices=(
        ("G", "Gasolina"),
        ("E", "Etanol"),
        ("D", "Diesel"),
        ("F", "Flex"),
        ("ET", "Elétrico"),
        ("H", "Híbrido"),
    ), max_length=20, db_column="Combustivel", verbose_name="Tipo de Combustível")

    def __str__(self):
        return f"{self.modelo} - {self.marca} ({self.ano})"
    
    class Meta:
        db_table = "Carro"
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ["modelo"]