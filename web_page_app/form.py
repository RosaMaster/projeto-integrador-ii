from django.forms import ModelForm
from .models import *
#from .models import Transacao, Consumidor


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']


class CadastroConsumidorForm(ModelForm):
    class Meta:
        model = Consumidor
        fields = ['registro_academico', 'nome', 'email', 'curso', 'senha']
