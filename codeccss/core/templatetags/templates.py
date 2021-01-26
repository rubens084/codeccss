from django import template
from django.contrib.auth.models import Group 
from core.models import *

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
       groups = user.groups.all().values_list('name', flat=True)
       return True if group_name in groups else False

@register.simple_tag
def loadsession(user):
       bandera=False
       data=Perfil.objects.get(user=user)
       if data.estado:
              bandera=True  
       return bandera