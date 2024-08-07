from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"


class Autor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ano_publicacao = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

