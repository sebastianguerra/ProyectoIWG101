from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from page.models import Pregunta, Respuesta, Test, Test_Realizacion



def home(request):
    ## Si el usuario que entra a la pagina no ha iniciado sesion:
    if not request.user.is_authenticated:
        return render(request, "guest.html")

def tests(request, id):
    test = Test.objects.get(id=id)
    preguntas = Pregunta.objects.filter(test=test)
    return render(request, "tests.html", {
        'preguntas': preguntas,
        'test': test,
    })

def resultados(request):
    pass

def about(request):
    pass

def procesar_preguntas(request):
    if request.method == "POST":
        test = Test.objects.get(id=request.POST["testID"])
        realizacion = Test_Realizacion(
            user=request.user,
            test=test,
        )
        realizacion.save()
        preguntas = Pregunta.objects.filter(test=test)    
        for pregunta in preguntas:
            respuesta = Respuesta(
                user=request.user,
                pregunta=pregunta,
                respuesta=int(request.POST[f"{pregunta.id}"]),
                test_realizacion=realizacion,
            )
            respuesta.save()
            print(respuesta.user, respuesta.pregunta, respuesta.respuesta, respuesta.test_realizacion)
        return HttpResponse("Todo bien:)")
    
