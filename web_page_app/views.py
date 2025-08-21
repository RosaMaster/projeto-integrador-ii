# web_page_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

# View para a página de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('conteudo')
    else:
        form = AuthenticationForm()
    return render(request, 'web_page_app/login.html', {'form': form})


# View para a página de Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('conteudo')
    else:
        form = UserCreationForm()
    return render(request, 'web_page_app/cadastro.html', {'form': form})


# View para a página de Reset de Senha (simplificada)
def reset_senha_view(request):
    return render(request, 'web_page_app/reset_senha.html')


# View para a página de Conteúdo (requer login)
@login_required(login_url='login')
def conteudo_view(request):
    pdf_path = '/media/documents/material.pdf'
    return render(request, 'web_page_app/conteudo.html', {'pdf_path': pdf_path})


# View para a página de Política e Termos de Uso
def politica_termos_view(request):
    return render(request, 'web_page_app/politica_termos.html')


# View para fazer o logout
def logout_view(request):
    logout(request)
    return redirect('login')
