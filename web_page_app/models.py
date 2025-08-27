from django.db import models
import uuid


class Curso(models.Model):
    nome = models.CharField(primary_key=True, unique=True, max_length=100)
    nome_abreviado = models.CharField(max_length=50, verbose_name='NomeAbreviado')
    duracao = models.PositiveIntegerField(verbose_name='Duracao')
    descricao = models.TextField(verbose_name='Descricao')

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    registro_academico = models.CharField(primary_key=True, unique=True, max_length=20)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.registro_academico


class Semana(models.Model):
    semana = models.PositiveIntegerField(primary_key=True, unique=True)

    def __str__(self):
        return str(self.semana)


class AnoLetivo(models.Model):
    ano = models.PositiveIntegerField(primary_key=True, unique=True)

    class Meta:
        verbose_name_plural = "Ano Letivo"

    def __str__(self):
        return str(self.ano)


class Disciplina(models.Model):
    codigo = models.CharField(primary_key=True, unique=True, max_length=10)         # Código único da disciplina
    nome = models.CharField(max_length=100)                                         # Nome da disciplina
    carga_horaria = models.PositiveIntegerField(verbose_name='Carga Horaria')       # Carga horária da disciplina
    descricao = models.TextField(verbose_name='Descricao')                          # Descrição da disciplina

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField(auto_created=True)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transacoes"

    def __str__(self):
        return self.descricao
    