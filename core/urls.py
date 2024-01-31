
from django.contrib import admin
from django.urls import path,include,re_path
from Tasks import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.CustomLogin.as_view(),name="login"),
    #path para asociar las rutas de las aplicaciones
    path("Tasks/",include("Tasks.urls"),name="Tasks"),
    #ruta para poder cerrar sesión 
    path('logout/',views.logout_view,name="logout"),
]
#url para poder ver los archivos media (documentospdf,img)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
