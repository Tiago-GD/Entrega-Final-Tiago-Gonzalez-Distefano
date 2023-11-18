from django.db import models
from ckeditor.fields import RichTextField


class Reloj(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = RichTextField()
    fecha_creacion = models.DateField()
    foto = models.ImageField(upload_to='FotoReloj', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo}'


