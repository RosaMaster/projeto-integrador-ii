# web_page_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.template_view, name='template'),
    path('template2/', views.template2_view, name='template2'),
    path('teste', views.teste_view, name='teste'),
    path('teste_update/<int:pk>/', views.teste_update, name='teste_update'),
    path('teste_delete/<int:pk>/', views.teste_delete, name='teste_delete'),
    #path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('reset-senha/', views.reset_senha_view, name='reset_senha'),
    path('conteudo/', views.conteudo_view, name='conteudo'),
    path('politica-termos/', views.politica_termos_view, name='politica_termos'),
    path('logout/', views.logout_view, name='logout_view'),
]
