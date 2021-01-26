from django import forms
from core.models import *

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model=Perfil

        fields=[
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            #'modulo',
            'email_institucional',
            'foto',
        ]

        labels={
            'nombre':'Ingrese nombre(s)',
            'apellido_paterno':'Ingrese apellido paterno',
            'apellido_materno':'Ingrese apellido materno',
            #'modulo':'Seleccione una modalidad',
            'email_institucional':'Correo institucional',
            'foto':'Fotografia'
        }
        
        widgets={
            'nombre': forms.TextInput(attrs={'type':'text','class':'form-control','id':'nombre','autocomplete':'off','placeholder':'Ingresa tu nombre'}),
            'apellido_paterno': forms.TextInput(attrs={'type':'text','class':'form-control','id':'apellidoPaterno','autocomplete':'off'}),
            'apellido_materno': forms.TextInput(attrs={'type':'text','class':'form-control','id':'apellidoMaterno','autocomplete':'off'}),
            #'modulo': forms.Select(attrs={'class':'form-control','id':'modulo'}),
            'email_institucional': forms.TextInput(attrs={'type':'text','class':'form-control','id':'email_institucional','autocomplete':'off'}),
            'foto': forms.FileInput(attrs={'class':'form-control custom-file-input','id':'foto'})

        }

        
class AltaPerfilForm(forms.ModelForm):
    class Meta:
        model=Perfil

        fields=[
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'modulo',
            'email_institucional',
            'foto',
        ]

        labels={
            'nombre':'Ingrese nombre(s)',
            'apellido_paterno':'Ingrese apellido paterno',
            'apellido_materno':'Ingrese apellido materno',
            'modulo':'Seleccione una modalidad',
            'email_institucional':'Correo institucional',
            'foto':'Fotografia'
        }
        
        widgets={
            'nombre': forms.TextInput(attrs={'type':'text','class':'form-control','id':'nombre','autocomplete':'off','placeholder':'Ingresa tu nombre'}),
            'apellido_paterno': forms.TextInput(attrs={'type':'text','class':'form-control','id':'apellidoPaterno','autocomplete':'off','placeholder':'Ingresa tu apellido paterno'}),
            'apellido_materno': forms.TextInput(attrs={'type':'text','class':'form-control','id':'apellidoMaterno','autocomplete':'off', 'placeholder':'Ingresa tu apellido materno'}),
            'modulo': forms.SelectMultiple(attrs={'class':'form-control select2bs4','id':'modulo','data-placeholder':'Seleccione modalidades deseadas','multiple':'multiple'}),
            'email_institucional': forms.TextInput(attrs={'type':'text','class':'form-control','id':'email_institucional','autocomplete':'off','placeholder':'Ingresa correo con formato xxxxx@tectijuana.edu.mx o xxxxx@tectijuana.tecnm.mx'}),
            'foto': forms.FileInput(attrs={'class':'form-control custom-file-input','id':'foto'})
        }

class AltaCredito(forms.ModelForm):
    class Meta:
        model=Credito

        fields=[
            'matricula',
            'user',
            'directorio'
        ]

class AltaDocumento(forms.ModelForm):
    class Meta:
        model=Documento_Servicio

        fields=[
            'matricula',
            'user',
            'directorio'
        ]