from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=15, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    data_criacao_cliente = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome.capitalize()


    