from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #View usada no login anterior
    #path('login/', views.login_usuario, name='login_usuario'),

    #urls para login e logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.painel_controle, name='painel_controle'),
    
    #urls para alteração de senha
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('alterar_senha/alterada/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #urls para reiniciar a senha
    path('reiniciar_senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reiniciar_senha/reiniciada', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/reiniciada/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #urls para cadastrar usuario
    path('registrar/', views.registrar, name='registrar'),

]
