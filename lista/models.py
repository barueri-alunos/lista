from django.db import models

# Create your models here.
class Pedido(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    nascimento = models.DateField()
    pedido = models.TextField()
    
    def __str__(self):
        return self.nome