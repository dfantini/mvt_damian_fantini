from django.db import models

# Create your models here.
class  MiFamilia(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField ()
    parentesco = models.CharField(max_length=30)