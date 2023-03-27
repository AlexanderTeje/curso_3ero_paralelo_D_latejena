from django.db import models

# Create your models here.
class duenomascota(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-"
        return texto.format(self.id, self.nombre, self.direccion, self.telefono)

    class Meta: db_table = 'duenomascota'


class animal(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion_consulta = models.TextField()
    estado = models.BooleanField(default=True)
    dueno = models.ForeignKey(duenomascota, on_delete=models.CASCADE)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-"
        return texto.format(self.id, self.nombre, self.descripcion_consulta, self.estado)

    class Meta: db_table = 'animal'