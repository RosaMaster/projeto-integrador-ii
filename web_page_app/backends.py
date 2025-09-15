# web_page_app/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
from .models import Consumidor

class ConsumidorBackend(BaseBackend):
    """
    Autentica usando Consumidor.registro_academico OU Consumidor.email.
    Se validar, retorna/gera um User "espelho" para a sessão do Django.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        try:
            consumidor = Consumidor.objects.get(
                Q(registro_academico=username) | Q(email=username)
            )
        except Consumidor.DoesNotExist:
            return None

        senha_stored = consumidor.senha or ""

        ok = False
        # 1) Tenta como hash (recomendado)
        try:
            ok = check_password(password, senha_stored)
        except Exception:
            ok = False

        # 2) Fallback TEMPORÁRIO: compara em texto puro
        if not ok and senha_stored == password:
            ok = True
            # Opcional: ao logar com sucesso em texto puro, atualiza para hash
            try:
                consumidor.senha = make_password(password)
                consumidor.save(update_fields=["senha"])
            except Exception:
                pass

        if not ok:
            return None

        # Se validou, mapeia/gera um User do Django para a sessão
        UserModel = get_user_model()
        username_for_user = consumidor.registro_academico  # chave estável

        user, created = UserModel.objects.get_or_create(
            username=username_for_user,
            defaults={
                "email": consumidor.email,
                "first_name": (consumidor.nome or "")[:30],
                # Se quiser impedir login direto pelo auth padrão:
                # "is_active": True,
            },
        )

        # Mantém e-mail em sincronia
        dirty = False
        if user.email != consumidor.email:
            user.email = consumidor.email
            dirty = True
        if dirty:
            user.save(update_fields=["email"])

        return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
