"""CODECC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('login_alumno/',views.login_alumno,name='login_alumno'),
    path('login_docente/',views.login_docente,name='login_docente'),
    path("salir/", views.logout, name='salir'),
    path('dashbord/',views.dashbord_docente,name='dashbord'),
    path('inicio_docente/',views.inicio_docente,name='inicio_docente'),
    path('editar_perfil/',views.editar_perfil,name='editar_perfil'),
    path('expediente/',views.expediente,name='expediente'),
    path('expedienteServicio/',views.expedienteServicio,name='expedienteServicio'),
    path('expediente/servicio/<int:id>',views.detalle_expediente_servicio,name="detalle_expediente_servicio"),
    path('expediente/<int:id>',views.detalle_expediente,name="detalle_expediente"),
    path('expediente_alumno/<matricula>',views.expedienteAlumno,name='expediente_alumno'),
    path('historial/',views.historial,name='historial'),
    path('modulo/',views.modulo,name='modulo'),
    path('alta_credito/',views.alta_credito,name='alta_credito'),

    # Vistas AJAX #
    path('Ajax_AltaExpediente/',views.Ajax_AltaExpediente,name='Ajax_AltaExpediente'),
    path('Ajax_AltaExpedienteServicio/',views.Ajax_AltaExpedienteServicio,name='Ajax_AltaExpedienteServicio'),
    path('Ajax_AltaDocumentoExpediente/',views.Ajax_AltaDocumentoExpediente,name="Ajax_AltaDocumentoExpediente"),
    path('Ajax_AltaDocumentoExpedienteServicio/',views.Ajax_AltaDocumentoExpedienteServicio,name="Ajax_AltaDocumentoExpedienteServicio"),
    path('Ajax_ConsultaHistorial/',views.Ajax_ConsultaHistorial,name="Ajax_ConsultaHistorial"),
    path('Ajax_RedactarCredito',views.Ajax_RedactarCredito,name="Ajax_RedactarCredito"),
    path('Ajax_GuardarHistorialCredito',views.Ajax_GuardarHistorialCredito,name="Ajax_GuardarHistorialCredito"),
    path('Ajax_GuardarPlantilla',views.Ajax_GuardarPlantilla,name="Ajax_GuardarPlantilla"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
