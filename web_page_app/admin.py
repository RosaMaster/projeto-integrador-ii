from django.contrib import admin
from .models import Categoria, Transacao, Disciplina, Semana, AnoLetivo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Disciplina)
admin.site.register(Semana)
admin.site.register(AnoLetivo)
