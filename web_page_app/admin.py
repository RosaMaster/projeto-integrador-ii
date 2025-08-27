from django.contrib import admin
from .models import *
# from .models import Categoria, Transacao, Disciplina, Semana, AnoLetivo, Curso, Usuario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Disciplina)
admin.site.register(Semana)
admin.site.register(AnoLetivo)
admin.site.register(Curso)
admin.site.register(Usuario)
