from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

preguntas = [
    {
        'texto': 'Te gusta el pan?', 'id': 1
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