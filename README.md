# projeto-integrador-ii
Este projeto envolve todos os alunos de quaisquer trilhas. Neste momento, os alunos já terão cursado disciplinas específicas e, por isto, existem itens opcionais que devem ser explorados quando alunos destas trilhas estiverem nos grupos.


## CRIANDO UM AMBIENTE VIRTUAL NA VISUAL STUDIO CODE `venv`

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

## :books: DOCUMENTAÇÃO E LINKS ÚTEIS

| Documentação                                                                                             |
| -------------------------------------------------------------------------------------------------------- |
| [Ambientes virtuais em Python](https://www.alura.com.br/artigos/ambientes-virtuais-em-python?utm_term=&utm_campaign=topo-aon-search-gg-dsa-artigos_conteudos&utm_source=google&utm_medium=cpc&campaign_id=11384329873_164240702375_703853654617&utm_id=11384329873_164240702375_703853654617&hsa_acc=7964138385&hsa_cam=topo-aon-search-gg-dsa-artigos_conteudos&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=aud-527303763294:dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=google&hsa_ver=3&gad_source=1&gad_campaignid=11384329873&gbraid=0AAAAADpqZID_G8Ba9vYHZbPsGcK5Sc753&gclid=Cj0KCQjwqebEBhD9ARIsAFZMbfwdkmn1_ZMTSaenOgbTQ9FBlhgSl8mt40JQoZrRnY2Xdtd0yvulnfQaArkpEALw_wcB) |
| [Python .gitignore - GitHub](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore) |
| []() |
| []() |

