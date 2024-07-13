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
#vistas basadas en clases
from django.urls import reverse
#create view 
from django.views.generic import ListView, CreateView, UpdateView,DeleteView 
from .forms import Usuarioform
from .models import Usuario
 #Clase para ejecutar el formulario de inicio de sesión
from django.contrib.auth.forms import UserCreationForm

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
                return "Tasks/listar_usuario"
            if user.is_interno:
                messages.success(self.request, "Inicio de sesión correctamente")  
                return "Tasks/"

# def index(request):
#     consulta_usuarios = Usuario.objects.all()
#     return render(request,"index.html",{'consulta_usuarios':consulta_usuarios})

# CERRAR SESION
def logout_view(request):
    logout(request)
    return redirect('login')

#CRUD usuarios
class listar_usuario(ListView):
    model = Usuario
    template_name = "listar_usuario.html" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.get_queryset() 
        return context

class Crear_usuarios(CreateView):
    model = Usuario
    form_class = Usuarioform
    template_name = 'modales/modalcrear.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse('Tasks:listar_usuario')

class  ActualizarUsuario(UpdateView):
    model = Usuario
    form_class = Usuarioform
    template_name = "modales/modal.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_success_url(self):
        return reverse("Tasks:listar_usuario") 
    
class Eliminar_usuario(DeleteView):
    model = Usuario
    template_name = "modales/usuario_confirm_delete.html"
    def get_success_url(self):
        return reverse("Tasks:listar_usuario")

#desahilitar y habilitar usuarios del aplicativo 
def deshabilitar_usuario(request,id):
    object_list = Usuario.objects.get(id=id)
    object_list.is_active = False
    object_list.is_staff = False
    object_list.save()
    messages.success(request,"Usuario deshabilitado correctamente")
    return redirect("Tasks:listar_usuario")

def habilitar_usuario(request,id):
    object_list = Usuario.objects.get(id=id)
    object_list.is_active = 1
    object_list.is_staff = 1
    object_list.save()
    messages.success(request,"Usuario habilitado correctamente")
    return redirect("Tasks:listar_usuario")