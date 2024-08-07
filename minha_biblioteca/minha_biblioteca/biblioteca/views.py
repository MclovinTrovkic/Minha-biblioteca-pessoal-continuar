from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LivroForm, PreferenciasForm
from .models import Livro

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'biblioteca/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'biblioteca/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('dashboard')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form})

@login_required
def dashboard(request):
    livros = Livro.objects.filter(usuario=request.user)
    cor_fundo = request.session.get('cor_fundo', '#ffffff')
    return render(request, 'biblioteca/dashboard.html', {'livros': livros, 'cor_fundo': cor_fundo})

@login_required
def personalizar(request):
    if request.method == 'POST':
        form = PreferenciasForm(request.POST)
        if form.is_valid():
            cor_fundo = form.cleaned_data['cor_fundo']
            request.session['cor_fundo'] = cor_fundo
            return redirect('dashboard')
    else:
        form = PreferenciasForm()
    return render(request, 'biblioteca/personalizar.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Autor, Categoria
from .queries import livros_por_autor, contagem_livros_por_usuario, livros_por_categoria

def livros_por_autor_view(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    livros = livros_por_autor(autor_id)
    return render(request, 'biblioteca/livros_por_autor.html', {'autor': autor, 'livros': livros})

def contagem_livros_view(request):
    contagem = contagem_livros_por_usuario()
    return render(request, 'biblioteca/contagem_livros.html', {'contagem': contagem})

def livros_por_categoria_view(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    livros = livros_por_categoria(categoria_id)
    return render(request, 'biblioteca/livros_por_categoria.html', {'categoria': categoria, 'livros': livros})
