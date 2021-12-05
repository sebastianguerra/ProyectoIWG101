from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse

from page.models import Pregunta, Respuesta, Test, Test_Realizacion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm


def home(request):
    usuario = request.user
    ## Si el usuario que entra a la pagina no ha iniciado sesion:
    if not usuario.is_authenticated:
        return render(request, "guest.html", {
            "testTypes": Test.objects.all(),
        })
    else:
        userTests= Test_Realizacion.objects.filter(user=usuario)
        tests = Test.objects.all()
        for test in tests:
            if len(userTests.filter(test=test))==0:
                return redirect(f"/test/{test.id}")
    return redirect('/resultados/')

@login_required
def tests(request, id):
    test = Test.objects.get(id=id)
    preguntas = Pregunta.objects.filter(test=test)
    return render(request, "tests.html", {
        'preguntas': preguntas,
        'test': test,
        'testTypes': Test.objects.all(),
    })

@login_required
def resultados(request):
    usuario = request.user
    userTests = Test_Realizacion.objects.filter(user=usuario)
    return render(request, "resultados_area.html", {
        "tests": userTests,
        "testTypes": Test.objects.all(),
    })

def about(request):
    pass

def procesar_preguntas(request):
    if request.method == "POST" and request.user.is_authenticated:
        test = Test.objects.get(id=request.POST["testID"])
        realizacion = Test_Realizacion(
            user=request.user,
            test=test,
        )
        realizacion.save()
        preguntas = Pregunta.objects.filter(test=test)    
        contador = {}  
        for pregunta in preguntas:
            respuesta = Respuesta(
                user=request.user,
                pregunta=pregunta,
                respuesta=int(request.POST[f"{pregunta.id}"]),
                test_realizacion=realizacion,
            )
            respuesta.save()
            if not pregunta.area in contador:
                contador[pregunta.area] = 0
            contador[pregunta.area] += respuesta.respuesta
        mayor = max(contador, key=lambda key: contador[key])
        realizacion.resultado = mayor
        realizacion.save()
        
        return redirect('/')
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()
        
    return render(request, "registration/register.html", {
        'form': form, 'testTypes': Test.objects.all(),
    })