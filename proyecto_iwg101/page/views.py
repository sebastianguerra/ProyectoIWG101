from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from page.models import Pregunta, Test



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
    i = 1
    de_acuerdo = 0
    desacuerdo = 0
    if request.method == "POST":
        for i in range(8):
            i += 1
            print(request.POST[f"{i}"])
            if request.POST[f"{i}"] == "0": 
                desacuerdo += 1
            else:
                de_acuerdo += 1 

    print("Deacuerdo: " + str(de_acuerdo))
    print("Desacuerdo: " + str(desacuerdo))
    return render(request, "resultados_area.html", {
        "valores": {
            "de_acuerdo": de_acuerdo,
            "desacuerdo": desacuerdo,
        }
    }) 
    
