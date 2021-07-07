from django.db import models
from django.utils import timezone

# Create your models here.
class EntradaAnimal(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombreAnimal = models.CharField(max_length=50)
    descripcion = models.TextField()
    creacion = models.DateTimeField(
        default=timezone.now)
    publicacion = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombreAnimal

