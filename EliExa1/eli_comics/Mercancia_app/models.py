from django.db import models

# Create your models here.
class merch(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    serie=models.CharField(max_length=50)
    precio=models.IntegerField()
    cant=models.IntegerField()

    def __str__(self):
        return self.nombre