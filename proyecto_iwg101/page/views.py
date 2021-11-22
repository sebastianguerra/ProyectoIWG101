from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

preguntas = [
    {
        'texto': 'Te gusta el pan?', 'id': 1, "area": "artes"
    },
    {
        'texto': 'comes queso?', 'id': 2
    },
    {
        'texto': 'programas?', 'id': 3
    },
    {
        'texto': 'quieres ser profe?', 'id': 4
    },
    {
        'texto': 'cuando vas a vestirte todo fachero?', 'id': 5
    },
    {
        'texto': 'manejas auto?', 'id': 6
    },
    {
        'texto': 'renuevas auto?', 'id': 7
    },
    {
        'texto': 'pq django es tan bkn?', 'id': 8
    },
]

context = {
    'preguntas': preguntas,
}



def home(request):
    ## Si el usuario que entra a la pagina no ha iniciado sesion:
    if not request.user.is_authenticated:
        return render(request, "guest.html")

def tests(request, id):
    return render(request, "test1.html", context)

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
    
