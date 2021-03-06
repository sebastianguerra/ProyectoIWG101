from django.shortcuts import redirect, render

from django.template.defaulttags import register

# Create your views here.

from django.http import HttpResponse

from page.models import Area, Pregunta, Respuesta, Test, Test_Realizacion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm

from .os_lib import read_json_file

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
    # TODO validar que id exista
    test = Test.objects.get(id=id)
    preguntas = Pregunta.objects.filter(test=test)
    return render(request, "tests.html", {
        'preguntas': preguntas,
        'test': test,
        'testTypes': Test.objects.all(),
    })

def read_areas() -> list:
    data = read_json_file('data/areas.json')
    return data

def read_ingresos() -> dict:
    data = read_json_file('data/ingresos.json')
    return data

@register.filter
def get_sueldo(dictionary: dict, key):
    return dictionary[key]["ingresos"]

datos_areas = read_areas()
datos_ingresos = read_ingresos()

@login_required
def resultados(request):
    # TODO verificar que el usuario haya realizado los tests
    
    # Negocio accediendo al modelo
    usuario = request.user
    
    userTests = Test_Realizacion.objects.filter(user=usuario)
    testTypes = Test.objects.all()
    Areas = Area.objects.all()

    respuestasUsuario = Respuesta.objects \
        .filter(user=usuario)
    
    ultimosTestsUsuario = []
    for test in testTypes:
        ultimosTestsUsuario.append(Test_Realizacion.objects.filter(user=usuario).filter(test=test).last())
    
    Respuestas_tests = []
    for test in ultimosTestsUsuario:
        Respuestas_tests += list(respuestasUsuario \
            .filter(test_realizacion=test))

    # Template
    context = {
        "tests": userTests ,
        "testTypes": testTypes,
        "Areas": Areas,
        "Respuestas": respuestasUsuario,
        "Preguntas": Pregunta.objects.all(),
        "Respuestas_tests": Respuestas_tests,
        "Colores": {
            "En lo que eres bueno": "rgba(0,0,200,0.2)",
            "Lo que amas": "rgba(200,0,0,0.2)",
        },
        "ultimosTestsUsuario": ultimosTestsUsuario,
        "datos_areas": datos_areas, 
        "datos_ingresos": datos_ingresos, 
    }

    return render(request, "resultados_area.html", context=context)

def about(request):
    # TODO implementar
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