from django.contrib import admin
from page.models import Area, Test, Pregunta, Test_Realizacion, Respuesta

# Register your models here.

admin.site.register(Area)
admin.site.register(Test)
admin.site.register(Pregunta)
admin.site.register(Test_Realizacion)
admin.site.register(Respuesta)