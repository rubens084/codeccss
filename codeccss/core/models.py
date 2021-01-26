from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

import os
# Create your models here.

#especialidad=(("Radio Tecnologico","Radio Tecnologico"),("Deportivo","Deportivo"),("Taller de investigacion","Taller de investigacion"))

class Modulo(models.Model):
    tipo=models.CharField(max_length=56, blank=False, null=False, unique=True)
    maximo=models.CharField(max_length=56, blank=False, null=False)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)
    
    class Meta:
        verbose_name="Modulo"
        verbose_name_plural="Modulos"
    def __str__(self):
        return str(self.tipo)

def rename_folder_photo(instance,filename):
    ext = filename.split('.')[-1]
    folder="Fotografia de perfiles/"+str(instance.nombre+" "+instance.apellido_paterno+" "+instance.apellido_materno)
    filename = "%s_%s.%s" % (str(instance.user.id),instance.nombre+" "+instance.apellido_paterno, ext)
    return os.path.join(folder,filename)

class Perfil(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    nombre=models.CharField(max_length=56, blank=False, null=False)
    apellido_paterno=models.CharField(max_length=56, blank=False, null=False)
    apellido_materno=models.CharField(max_length=56, blank=False, null=False)
    modulo=models.ManyToManyField(Modulo, blank=True)
    email_institucional=models.CharField(max_length=126, blank=False, null=False, validators=[RegexValidator(regex=r'(^[a-zA-Z0-9_.+-]+@tectijuana.edu.mx+$)|(^[a-zA-Z0-9_.+-]+@tectijuana.tecnm.mx+$)',message="El formato del correo debe ser @tectijuana.edu.mx")])
    foto=models.ImageField(upload_to=rename_folder_photo, max_length=126, blank=True, null=True)
    estado=models.BooleanField(default=False)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)

    class Meta:
        verbose_name="Perfil"
        verbose_name_plural="Perfiles"
    def __str__(self):
        return "Perfil del usuario "+str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno)

class Expediente(models.Model):
    matricula=models.CharField(max_length=56, blank=False, null=False)
    nombre=models.CharField(max_length=56, blank=False, null=False)
    apellido_paterno=models.CharField(max_length=56, blank=False, null=False)
    apellido_materno=models.CharField(max_length=56, blank=False, null=False)
    perfil=models.ForeignKey(Perfil, null=True,on_delete=models.SET_NULL)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)
    
    class Meta:
        verbose_name="Expediente"
        verbose_name_plural="Expedientes"
    def __str__(self):
        return str(self.matricula)

def rename_folder_credito(instance,filename):
    ext = filename.split('.')[-1]
    folder="Creditos/"+str(instance.matricula)
    return os.path.join(folder,filename)

class Credito(models.Model):
    matricula=models.ForeignKey(Expediente , null=True,on_delete=models.SET_NULL)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    directorio=models.FileField(upload_to=rename_folder_credito, max_length=126, blank=True, null=True)
    rubro=models.CharField(max_length=126, blank=True, null=True)
    nombre=models.CharField(max_length=126, blank=True, null=True)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)

    class Meta:
        verbose_name="Credito"
        verbose_name_plural="Creditos"
    def __str__(self):
        return str(self.matricula)

class Plantilla(models.Model):
    archivo=models.FileField(upload_to="Plantillas/", max_length=126)
    user=models.ForeignKey(User, null=True,on_delete=models.SET_NULL, blank=True)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)

    class Meta:
        verbose_name="Plantilla"
        verbose_name_plural="Plantillas"
    
    def __str__(self):
        return str(self.archivo)

class Historial_Redaccion(models.Model):
    matricula=models.CharField(max_length=56, blank=False, null=False)
    nombre=models.CharField(max_length=126, blank=False, null=False)
    carrera=models.CharField(max_length=126, blank=False, null=False)
    modulo=models.CharField(max_length=126, blank=False, null=False)
    valor=models.IntegerField(blank=False, null=False)
    jefa=models.CharField(max_length=126, blank=False, null=False)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)

    class Meta:
        verbose_name_plural="Historial de Redaccion"
    
    def __str__(self):
        return str(self.matricula)

class Expediente_Servicio(models.Model):
    matricula=models.CharField(max_length=56, blank=False, null=False)
    nombre=models.CharField(max_length=56, blank=False, null=False)
    apellido_paterno=models.CharField(max_length=56, blank=False, null=False)
    apellido_materno=models.CharField(max_length=56, blank=False, null=False)
    perfil=models.ForeignKey(Perfil, null=True,on_delete=models.SET_NULL)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)

    class Meta:
        verbose_name="Expediente de Servicio"
        verbose_name_plural="Expedientes de Servicio"
    def __str__(self):
        return str(self.matricula)


def rename_folder_documento(instance,filename):
    ext = filename.split('.')[-1]
    folder="Servicio/"+str(instance.matricula)
    return os.path.join(folder,filename) 

class Documento_Servicio(models.Model):
    matricula=models.ForeignKey(Expediente_Servicio , null=True, on_delete=models.SET_NULL)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    directorio=models.FileField(upload_to=rename_folder_documento, max_length=126, blank=True, null=True)
    nombre=models.CharField(max_length=126, blank=True, null=True)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField("Creado ", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado ", auto_now=True)
    
    class Meta:
        verbose_name="Documento de Servicio"
        verbose_name_plural="Documentos de Servicio"
    def __str__(self):
        return str(self.matricula)