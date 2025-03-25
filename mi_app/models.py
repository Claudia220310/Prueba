from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/')
    video = models.FileField(upload_to='videos/')
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.nombre
