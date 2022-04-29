from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Services(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombre')
    image = models.ImageField(default='Null', verbose_name="Imagen", upload_to="services" )
    description = models.CharField(max_length=255, verbose_name='Descripcion' )
    #info = models.TextField(verbose_name="Informacion")
    info = RichTextField(verbose_name="Informacion")
    public = models.BooleanField(default=True,  verbose_name='¿Visible?')
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateField(auto_now=True, verbose_name="Ultima Actualizacion")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name