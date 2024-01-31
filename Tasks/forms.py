#formularios
from django import forms
#modelos
from Tasks.models import Usuario
#formularios de creacion 
from django.contrib.auth.forms import UserCreationForm
#validacion de errores 
from django.core.exceptions import ValidationError


#clase para crear el registro de usuario externo (formulario)
class Usuarioform(UserCreationForm):
    email = forms.EmailField(required=True,label="Correo electronico",max_length=50,
    error_messages={'invalid':'solo puedes colocar caracteres validos'})

    class Meta (UserCreationForm):
        model = Usuario
        fields = ('dni','email','nombres','apellidos','tipo_documento','password1','password2')
    def clean(self):
        cleaned_data =super().clean()
        #validaciones necesarias en el formulario
        nombres = cleaned_data.get('nombres')
        apellidos = cleaned_data.get('apellido')
        if nombres and apellidos:
            if nombres == apellidos:
                raise forms.ValidationError ("los nombres y apellidos no pueden ser iguales.")
        return cleaned_data
        
#registro de usuario Externo (validacion)
class UsuarioexternoForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Correo electrónico',max_length=50,
        error_messages={'invalid':'solo puedes colocar caracteres validos para el correo'})
    class Meta(UserCreationForm):
        model=Usuario
        fields=('dni','email','nombres','apellidos','tipo_documento','password1','password2')
    def clean_email(self):
        email=self.cleaned_data['email']
        u = Usuario.objects.filter(email=email)
        if u.count():
            raise ValidationError('correo electronico ya ha sido tomado')
        return email        
    

#CLASE PARA LOS USUARIOS ADMINISTRADOR
class Usuariosform(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('dni','nombres','apellidos','email','tipo_documento')    