# web_page_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Transacao
from datetime import datetime
from .form import TransacaoForm, CadastroConsumidorForm

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
def home_view(request):
    data = {}

    return render(request, 'web_page_app/home.html', data)


# View para a página de Cadastro
def cadastro_view(request):
    data = {}
    if request.method == 'POST':
        form = CadastroConsumidorForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CadastroConsumidorForm()

    data['form'] = form

    return render(request, 'web_page_app/cadastro.html', data)


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


def teste_view(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.now()

    data['all_transacoes'] = Transacao.objects.all()

    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('teste')

    data['form'] = form

    return render(request, 'web_page_app/teste.html', data)


# def nova_transacao(request):
#     data = {}
    
#     form = TransacaoForm()

#     data['form'] = form

#     return render(request, 'web_page_app/teste.html', data)


def teste_update(request, pk):
    data = {}

    transacao = Transacao.objects.get(pk=pk)

    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('teste')

    data['form'] = form
    data['transacao'] = transacao

    return render(request, 'web_page_app/teste_update.html', data)


def teste_delete(request, pk):

    transacao = Transacao.objects.get(pk=pk)

    transacao.delete()

    return redirect('teste')

def template_view(request):
    data = {}
    data['now'] = datetime.now()

    return render(request, 'web_page_app/template.html')

def template2_view(request):
    data = {}
    data['now'] = datetime.now()

    return render(request, 'web_page_app/template2.html')