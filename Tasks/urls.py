from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve
from Tasks import views
app_name = "Tasks"
urlpatterns = [
    #registro usuarios
    path("registro/",views.ir_registro,name="registro_usuarios"),
    #inicio login
    path("",views.inicio_login,name="inicio_login"),
    path("index/",views.index,name="index"),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
