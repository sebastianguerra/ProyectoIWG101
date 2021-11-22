from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    pass

class Test(models.Model):
    pass

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.text}, {self.area}"

class Test_Realizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicial = models.DateField()
    fecha_last_update = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    resultado = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.fecha_inicial}"

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.IntegerField()
    test_realizacion = models.ForeignKey(Test_Realizacion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.respuesta}"