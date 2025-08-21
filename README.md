# projeto-integrador-ii
## TEMA: Portal de Conteúdo
### GRUPO - DRP01-PJI240-SALA-003GRUPO-019

Este projeto envolve alunos do eixo da Computação da Universidade __UNIVESP__.

#### DESAFIO

Desenvolvimento web, construir websites funcionais e disponibilizá-los na nuvem para poderem ser acessados por qualquer pessoa em qualquer lugar do mundo. Incluir algumas funcionalidades importantes que serão vistas ao longo do semestre, como:
- acessibilidade
- linguagens de script
- nuvem
- etc

## :tada: CRIANDO UM AMBIENTE VIRTUAL NA VISUAL STUDIO CODE `venv`

<details><summary>Como criar uma ambiente virtual VENV</summary>

#### O que é uma `venv` ?

Uma __venv__ (abreviação de virtual environment, ou ambiente virtual) é uma ferramenta essencial no ecossistema do Python. A sua principal função é criar um ambiente isolado e autocontido para cada projeto Python. Pense nela como uma caixa de ferramentas separada para cada projeto que você trabalha.

**OBSERVAÇÃO**: Nunca suba para o repositório or arquivos e o diretório `venv`, antes de subir qualquer commit remoto verificar se consta o arquivo `.gitignore`.

<details><summary>Criando venv pelo terminal Prompt de Comando CMD</summary>

- Execute o comando abaixo na raiz do projeto via prompt de comando:

~~~Shell
python -m venv venv
~~~

- Após criar seu ambiente virtual para o projeto atual. Ative o ambiente virtual com o comando abaixo:

~~~Shell
venv\Scripts\activate
~~~

- Caso queira desativar o ambiente virtal é só executar o comando abaixo:

~~~Shell
deactivate
~~~

</details>

<br>

<details><summary>Criando venv pelo terminal Git Bash</summary>

- Execute o comando abaixo na raiz do projeto via prompt de comando:

~~~Bash
python -m venv venv
~~~

- Após criar seu ambiente virtual para o projeto atual. Ative o ambiente virtual com o comando abaixo:

~~~Bash
source venv/Scripts/activate
~~~

- Caso queira desativar o ambiente virtal é só executar o comando abaixo:

~~~Bash
deactivate
~~~

</details>

<br>

- Validando as bibliotecas instaladas na `venv`:

~~~Bash
pip list
~~~

- Se precisar atualizar a versão do `pip`, execute:

~~~Bash
python.exe -m pip install --upgrade pip
~~~

- Instalando uma biblioteca:

~~~Bash
pip install nome_da_biblioteca
~~~

- Desinstalar uma biblioteca:

~~~Bash
pip uninstall nome_da_biblioteca
~~~

- Criando arquivo `requirements.txt`:

~~~Bash
pip freeze > requirements.txt
~~~

- Instalando bibliotecas do arquivo `requirements.txt`, se ele existir:

~~~Bash
pip install -r requirements.txt
~~~

</details>

## :rocket: INSTALANDO E EXECUTANDO DJANGO REST FRAMEWORK

<details><summary>O que é Django Rest Framework</summary><br>

__Django__ é um framework web de alto nível para Python que incentiva o desenvolvimento rápido e um design limpo e pragmático. Ele foi criado para simplificar o processo de construção de sites e aplicações web complexas, cuidando de grande parte do trabalho pesado por você.

- Instalando a biblioteca `django`

~~~Bash
pip install django
~~~

- Agora você pode usar o comando `django-admin` para criar a estrutura básica do seu projeto, conforme exemplo:<br>
`OBS: O ponto no final é crucial. Ele informa ao Django para criar os arquivos do projeto no diretório atual, evitando uma pasta aninhada desnecessária`

~~~Bash
django-admin startproject nome_do_seu_projeto .
~~~

- Após criar o projeto, o `Django` precisa configurar o banco de dados inicial, para isso, execute o comando `migrate`<br>
`Este comando criará as tabelas necessárias para os aplicativos padrão do Django (autenticação de usuários, sessões, etc.)`

~~~Bash
python manage.py migrate
~~~

- Para ver seu projeto em ação, inicie o servidor de desenvolvimento do `Django`, execute o comando `runserver`:

~~~Bash
python manage.py runserver
~~~

Agora, abra seu navegador e acesse o endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Se tudo deu certo, você verá a página de boas-vindas do Django, indicando que seu projeto foi criado com sucesso.

:clap: Pronto! Seu projeto __Django__ está configurado e pronto para você começar a ser desenvolvido.

<details><summary>Crie um Aplicativo Django</summary>

- Projetos `Django` são divididos em "**aplicativos**". É uma boa prática criar um aplicativo para cada funcionalidade principal do seu site.<br>
`OBS: Certifique-se de que sua venv esteja ativada e que você esteja no diretório raiz do seu projeto (onde está o manage.py). Isso criará uma nova pasta chamada core (ou o nome que você escolher para seu aplicativo) dentro do seu projeto.`

~~~Bash
python manage.py startapp core
~~~

- Registre o Aplicativo, após criar o aplicativo, você precisa registrá-lo no seu projeto Django. Abra o arquivo nome_do_seu_projeto/settings.py (dentro da pasta principal do seu projeto). Procure a lista INSTALLED_APPS e adicione o nome do seu aplicativo ('core') a ela.

~~~Python
# nome_do_seu_projeto/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Adicione esta linha
]
~~~

- Crie a View (Lógica da Página).
`OBS: A view é uma função Python que recebe uma requisição web e retorna uma resposta web. Abra o arquivo core/views.py. Adicione o seguinte código para criar uma view que retorna "Hello World".`

~~~Python
# core/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")
~~~

-  Defina as URLs do Aplicativo
`OBS: Agora você precisa dizer ao Django qual URL deve ser mapeada para a sua view home. Dentro da pasta core, crie um novo arquivo chamado urls.py. Adicione o seguinte código a core/urls.py`<br>
`path('', views.home, name='home'): Este é o mapeamento. O '' indica uma URL vazia, ou seja, a raiz do seu aplicativo. Quando alguém acessa essa URL, a função views.home será chamada. name='home' é um nome opcional para esta URL, útil para referenciá-la em outras partes do seu código Django.`

~~~Python
# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
~~~

- Inclua as URLs do Aplicativo no Projeto Principal
`OBS: Por fim, você precisa incluir as URLs do seu aplicativo (core/urls.py) no arquivo de URLs principal do seu projeto. Abra o arquivo nome_do_seu_projeto/urls.py (o arquivo principal, não o do seu aplicativo core). Adicione a função include e inclua as URLs do seu aplicativo`<br>
`path('', include('core.urls')): Isso significa que qualquer requisição para a raiz do seu site ('') será "delegada" ao arquivo core/urls.py para ser resolvida`

~~~Python
# nome_do_seu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Adicione esta linha
]
~~~

- Teste Sua Página

~~~Bash
python manage.py runserver
~~~

- Abra seu navegador e vá para [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Você deve ver a mensagem "Hello World!" na tela.

:star: Sua primeira página Django está configurada! PARABÉNS!

</details>

</details>

## :suspect: CREATE SUPER USER

<details><summary>Como criar user admin</summary>

- Execute o comando abaixo:

~~~Bash
python manage.py createsuperuser
~~~

- Em seguida informe o nome do super-usuario a ser criado:

Ex: admin

- Informe a senha de acesso desse superuser, será necessário informar duas vezes!

- Abra seu navegador e vá para [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Você deve ver a tela de login use o usuario criado "admin" e o "password" cadastrado.

</details>

## EXECUTE APLICAÇÃO

- Sempre executar os camndos abaixo em sequencia:

~~~Bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

- Abra seu navegador e vá para [http://127.0.0.1:8000](http://127.0.0.1:8000). Você deve ver a tela de login use o usuario criado "admin" e a senha "admin123" cadastrado.

## :suspect: CREATE TEMPLATES COM VIEWS

## :suspect: CREATE TABLES COM MODELS

## :books: DOCUMENTAÇÃO E LINKS ÚTEIS

| Documentação                                                                                                   |
| -------------------------------------------------------------------------------------------------------------- |
| [Ambientes virtuais em Python](https://www.alura.com.br/artigos/ambientes-virtuais-em-python?utm_term=&utm_campaign=topo-aon-search-gg-dsa-artigos_conteudos&utm_source=google&utm_medium=cpc&campaign_id=11384329873_164240702375_703853654617&utm_id=11384329873_164240702375_703853654617&hsa_acc=7964138385&hsa_cam=topo-aon-search-gg-dsa-artigos_conteudos&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=aud-527303763294:dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=google&hsa_ver=3&gad_source=1&gad_campaignid=11384329873&gbraid=0AAAAADpqZID_G8Ba9vYHZbPsGcK5Sc753&gclid=Cj0KCQjwqebEBhD9ARIsAFZMbfwdkmn1_ZMTSaenOgbTQ9FBlhgSl8mt40JQoZrRnY2Xdtd0yvulnfQaArkpEALw_wcB) |
| [Python .gitignore - GitHub](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore)       |
| [Django The web framework for perfectionists with deadlines.](https://docs.djangoproject.com/en/5.2/releases/) |
| []() |
