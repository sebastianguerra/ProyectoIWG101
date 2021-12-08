from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse

from page.models import Area, Pregunta, Respuesta, Test, Test_Realizacion
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


datos = [
    {
        "area": "Artes",
    "carreras": ["Teatro", "Arquitectura", "Cine", "Diseño Grafico", "Musica"],
    "mensaje": "El mundo necesita inspiración y tú necesitas expresarte, estás son las carreras para ti:"
    },
    {
        "area": "Ciencias de la salud",
    "carreras": ["Enfermeria", "Medicina", "Kinesiologia", "Obstetricia", "Odontologia"],
    "mensaje": "El mundo necesita gente con vocación para sanar, estás son las carreras para ti:"
    },
    {
        "area": "Ingenieria y Carreras afines",
    "carreras": ["Ingenieria plan comun", "ingenieria en computacion e informatica", "Ingenieria en fisica"],
    "mensaje": "El mundo necesita gente con visión y ganas de innovar, estás son las carreras para ti:"
    },
    {
        "area": "Biología y química",
    "carreras": ["Biologia", "Biotecnologia", "Quimica y farmacia"],
    "mensaje": "El mundo necesita progresos en la ciencia, estás son las carreras para ti:"
    },
    {
        "area": "Educacion",
    "carreras": ["Psicopedagogia", "Pedagogia en ingles", "Pedagogia en lenguaje", "Pedagogia en matematicas"],
    "mensaje": "El mundo necesita progresos en la ciencia, estás son las carreras para ti:"
    },
    {
        "area": "Letras y humanidades",
    "carreras": ["Derecho", "Periodismo", "Ciencias politicas", "Literatura"],
    "mensaje": "El mundo necesita progresos en la ciencia, estás son las carreras para ti:"
    },
]
  
datos2 = [
    {
        "carrera": "Teatro",
    "ingresos": "700 000",
    },
    {
        "carrera": "Arquitectura",
    "ingresos": "1 500 000",
    },
    {
        "carrera": "Cine",
    "ingresos": "800 000",
    },
    {
        "carrera": "Diseño Grafico",
    "ingresos": "600 000",
    },
    {
        "carrera": "Musica",
    "ingresos": "360 000 - 1 200 000",
    },
    {
        "carrera": "Biologia",
    "ingresos": "750 000",
    },
    {
        "carrera": "Biotecnologia",
    "ingresos": "850 000",
    },
    {
        "carrera": "Quimica y farmacia",
    "ingresos": "1 200 000",
    },
    {
        "carrera": "Ingenieria en quimica",
    "ingresos": "1 000 000",
    },
    {
        "carrera": "Ingenieria en alimentos",
    "ingresos": "600 000",
    },
    {
        "carrera": "Enfermeria",
    "ingresos": "1 500 000",
    },
    {
        "carrera": "Medicina",
    "ingresos": "2 000 000",
    },
    {
        "carrera": "Kinesiologia",
    "ingresos": "1 000 000",
    },
    {
        "carrera": "Obstetricia",
    "ingresos": "800 000",
    },
    {
        "carrera": "Odontologia",
    "ingresos": "800 000",
    },
    {
        "carrera": "Psicopedagogia",
    "ingresos": "750 000",
    },
    {
        "carrera": "Pedagogia en ingles",
    "ingresos": "600 000",
    },
    {
        "carrera": "Pedagogia en Lenguaje",
    "ingresos": "600 000",
    },
    {
        "carrera": "Pedagogia en matematicas",
    "ingresos": "600 000",
    },
    {
        "carrera": "Derecho",
    "ingresos": "2 000 000",
    },
    {
        "carrera": "Periodismo",
    "ingresos": "800 000",
    },
    {
        "carrera": "Ciencias politicas",
    "ingresos": "3 000 000",
    },
    {
        "carrera": "Literatura",
    "ingresos": "800 000 - 1 300 000",
    },
    {
        "carrera": "Idiomas y traduccion",
    "ingresos": "700 000",
    },
    {
        "carrera": "Ingenieria plan comun",
    "ingresos": "800 000",
    },
    {
        "carrera": "Ingenieria en computación e informatica",
    "ingresos": "1 200 000",
    },
    {
        "carrera": "Ingenieria en fisica",
    "ingresos": "1 000 000",
    },
]

@login_required
def resultados(request):
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

    return render(request, "resultados_area.html", {
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
        "datos": datos, 
        "datos2": datos2, 
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