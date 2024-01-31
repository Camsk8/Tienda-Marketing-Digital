#retornos 
from django.shortcuts import render,redirect 
#sweet alert 
from django.contrib import messages
#inicio de sesión
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from Tasks.forms import Usuarioform, Usuariosform,UsuarioexternoForm
from Tasks.models import Usuario
#cerrar sesión
from django.contrib.auth import logout



#from django.http import HttpResponse (import para poder redirigir a la vista que se defina )
from django.contrib.auth.forms import UserCreationForm #Clase para ejecutar el formulario de inicio de sesión
# Create your views here.
# def index(request):
#     return render(request, 'index.html',{
#         'form':UserCreationForm
#     })

# funcion para ir a la pagina de registro
def ir_registro(request):
    form = UsuarioexternoForm()
    if request.method == 'POST':
        form = UsuarioexternoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario creado correctamente')
            return redirect('login')
    return render (request,"registration/registro.html",{'form':form})
    
# funcion que retorna a la pagina de inicio cuando se ha logueado correctamente
def inicio_login(request):
    return render(request,'registration/profile.html',{})

#modelo de inicio de sesion personalizado
#vistas basadas en clases
class CustomLogin(LoginView):
    form_class = AuthenticationForm
    template_name ="registration/login.html"
    success_url = "/"
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_admin:
                messages.success(self.request, "Inicio de sesión correctamente")    
                return "Tasks/index"
            if user.is_interno:
                messages.success(self.request, "Inicio de sesión correctamente")  
                return "Tasks/"

def index(request):
    consulta_usuarios = Usuario.objects.all()
    return render(request,"index.html",{'consulta_usuarios':consulta_usuarios})

# CERRAR SESION
def logout_view(request):
    logout(request)
    return redirect('login')
