from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve
from . import views
from Tasks.views import listar_usuario ,Crear_usuarios,ActualizarUsuario,Eliminar_usuario
app_name = "Tasks"
urlpatterns = [
    #registro usuarios
    path("registro/",views.ir_registro,name="registro_usuarios"),
    #inicio login
    path("",views.inicio_login,name="inicio_login"),
    # path("index/",views.index,name="index"),
    #clases CRUD usuarios
    path("listar_usuario/", listar_usuario.as_view(), name="listar_usuario"),
    path('crear_usuarios/',Crear_usuarios.as_view(),name='crear_usuarios'),
    path('actualizar_usuario/<int:pk>/',ActualizarUsuario.as_view(),name='actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',Eliminar_usuario.as_view(),name='eliminar_usuario'),
    #deshabilitar y habilitar usuarios ADMIN
    path('Tasks/deshabilitar_usuario/<int:id>/', views.deshabilitar_usuario, name='deshabilitar_usuario'),
    path('habilitar_usuario/<int:id>/',views.habilitar_usuario,name='habilitar_usuario'),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
