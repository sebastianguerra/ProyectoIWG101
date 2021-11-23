from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.texto}, {self.area}"

class Test_Realizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicial = models.DateField(auto_now_add=True)
    fecha_last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    resultado = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.fecha_inicial}, {self.test.nombre}"

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.IntegerField()
    test_realizacion = models.ForeignKey(Test_Realizacion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user}, {self.respuesta}, {self.test_realizacion}"