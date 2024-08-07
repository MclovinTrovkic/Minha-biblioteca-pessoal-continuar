from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('personalizar/', views.personalizar, name='personalizar'),
    path('livros_por_autor/<int:autor_id>/', views.livros_por_autor_view, name='livros_por_autor'),
    path('contagem_livros/', views.contagem_livros_view, name='contagem_livros'),
    path('livros_por_categoria/<int:categoria_id>/', views.livros_por_categoria_view, name='livros_por_categoria'),
]

