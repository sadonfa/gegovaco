from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(models.Model):
            
    name   = models.CharField(max_length=150, verbose_name='Nombre y Apellido')
    mail = models.EmailField(verbose_name='Correo')
    phone  = models.CharField(max_length=100, verbose_name='Telefono')
    mess = RichTextField(verbose_name='Mensaje')
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateField(auto_now=True, verbose_name="Ultima Actualizacion")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name