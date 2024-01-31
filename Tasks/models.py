from django.db import models
#(AbstractBaseUser)Al heredar de esta clase, puedes definir tu propio modelo de usuario,incluyendo campos adicionales
#(PermissionsMixin)proporciona campos y métodos para gestionar permisos de usuario
from django.contrib.auth.models import  AbstractBaseUser , PermissionsMixin
#clase base para la creación de gestores de usuarios personalizados 
from django.contrib.auth.base_user import BaseUserManager
#permite la traduccion de cadenas de texto
from django.utils.translation import gettext_lazy as _
#manejo de hora en la aplicación
from django.utils import timezone
#configuracion de rutas 
import os

#Modelo tipo de documento  
class TipoDocumento(models.Model):
    nombre=models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
    class  Meta:
        db_table = 'tipo_documento'

#herencia del modelo BaseUserManager
class UsuarioManager(BaseUserManager):
    #crea un usuario basico
    def create_user(self,email,password,**extra_fields):
        #si no tiene email , se detiene y muestra error
        if not email:
            raise ValueError('correo electronico es necesario!!')
        #si hay email, continua con lo siguiente
        email = self.normalize_email(email)
        usuario = self.model(email=email,**extra_fields)
        #utilizamos la encriptacion para la contraseña y la guarda en el mismo campo
        usuario.set_password(password)
        usuario.save()
        return usuario

# Clase Para crear usuario administrador
    def create_superuser(self,email,password,**extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff",True) 
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(email,password,**extra_fields)
    #caracteristicas del administrador
        usuario.set_password(password)
        usuario.user_admin = True
        return usuario
 
   
class Usuario(AbstractBaseUser):
    dni=models.CharField("Identificacion",max_length=255,unique=True)
    email = models.EmailField('correo electronico',unique=True,max_length=255)
    nombres = models.CharField('nombres', max_length=100,blank=True,null=True)
    apellidos = models.CharField('apellidos', max_length=100,blank=True,null=True)
    tipo_documento=models.ForeignKey(TipoDocumento,on_delete=models.CASCADE,null=True,default=None)   
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #modelos Relacionados con el tipo de usuario
    is_admin=models.BooleanField(default=False)
    is_interno=models.BooleanField(default=True)
    #enlazamos con la clase usuario manager
    objects=UsuarioManager()
    is_superuser=models.BooleanField(default=False)
    username=None
    #parametro unico, siempre requerido
    USERNAME_FIELD="email"
    #Campos requeridos
    REQUIRED_FIELDS=['dni']
    #me retorna en nombre de correo electonico 
    def _str_(self):
        return self.email
    #permisos de quien puede acceder al admin de django 
    def has_perm(self,perm,obj=None):
        return True
    #admin django 
    def has_module_perms(self,app_label):
        return True

    class  Meta:
        db_table = 'Usuario'
