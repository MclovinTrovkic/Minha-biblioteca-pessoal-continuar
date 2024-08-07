from django.db.models import Count
from .models import Livro, Autor, Categoria

def livros_por_usuario(usuario):
    return Livro.objects.filter(usuario=usuario).order_by('titulo')

def livros_por_autor(autor_id):
    return Livro.objects.filter(autor_id=autor_id).order_by('titulo')

def contagem_livros_por_usuario():
    return Livro.objects.values('usuario').annotate(contagem=Count('id')).order_by('-contagem')

def livros_por_categoria(categoria_id):
    return Livro.objects.filter(categoria_id=categoria_id).order_by('titulo')
