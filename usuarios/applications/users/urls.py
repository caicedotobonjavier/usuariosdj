from django.urls import path, re_path, include
#
from . import views


app_name = 'users_app'

urlpatterns = [
    path('crear-usuario/', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('login-usuario/', views.LoginUserView.as_view(), name='login_usuario'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #
    path('update-password/', views.ActualizarPasswordView.as_view(), name='update_password'),
    path('update-info/<pk>/', views.UpdateInfoUserView.as_view(), name='update_info'),
    path('verificar-codigo/<pk>/', views.VerificacionCodigoView.as_view(), name='verificar_codigo'),
]