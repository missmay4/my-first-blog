from django.db import models
from django.utils import timezone

class Post(models.Model): #modelo del blog, cosas que hay dentro como autor, titulo, textos, fechas...
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #metodo para poder publicar en el blog
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #metodo para el nombre del blog
        return self.title
