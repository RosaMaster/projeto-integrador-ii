# web_page_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.template_view, name='template'),
    path('teste', views.teste_view, name='teste'),
    path('teste_update/<int:pk>/', views.teste_update, name='teste_update'),
    path('teste_delete/<int:pk>/', views.teste_delete, name='teste_delete'),
    #path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('reset-senha/', views.reset_senha_view, name='reset_senha'),
    path('conteudo/', views.conteudo_view, name='conteudo'),
    path('politica-termos/', views.politica_termos_view, name='politica_termos'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', auth_views.LoginView.as_view(
        template_name='web_page_app/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
