from django.shortcuts import render

# Create your views here.


def home(request):
    
    ## Si el usuario que entra a la pagina no ha iniciado sesion:
    if not request.user.is_authenticated:
        return render(request, "guest.html")

def tests(request, id):
    pass

def resultados(request):
    pass

def about(request):
    pass