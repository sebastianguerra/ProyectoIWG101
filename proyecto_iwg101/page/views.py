from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from page.models import Pregunta, Respuesta, Test, Test_Realizacion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm


def home(request):
    usuario = request.user
    ## Si el usuario que entra a la pagina no ha iniciado sesion:
    if not usuario.is_authenticated:
        return render(request, "guest.html")
    else:
        userTests= Test_Realizacion.objects.filter(user=usuario)
        if len(userTests.filter(test=Test.objects.get(id=1)))==0:
            return redirect('/test/1')
        elif len(userTests.filter(test=Test.objects.get(id=2)))==0:
            return redirect('/test/2')
        else:
            return redirect('/resultados/')

@login_required
def tests(request, id):
    test = Test.objects.get(id=id)
    preguntas = Pregunta.objects.filter(test=test)
    return render(request, "tests.html", {
        'preguntas': preguntas,
        'test': test,
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
        for pregunta in preguntas:
            respuesta = Respuesta(
                user=request.user,
                pregunta=pregunta,
                respuesta=int(request.POST[f"{pregunta.id}"]),
                test_realizacion=realizacion,
            )
            respuesta.save()
            print(respuesta.user, respuesta.pregunta, respuesta.respuesta, respuesta.test_realizacion)
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
        
    context = {'form': form}
    return render(request, "registration/register.html", context)