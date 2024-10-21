from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)  
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.post.titulo}"
