#!/usr/bin/env python3
import json, sys

def lastDir(dir):
    return dir.split("/")[-1].split("\\")[-1]

if __name__ == "__main__":
    print("Importar modelos desde un json")
    
    
    ## Verifico que se haya dado un nombre o no
    argumentos = sys.argv
    while not lastDir(__file__) == lastDir(argumentos[0]):
        argumentos = argumentos[1:]
    argumentos = argumentos[1:]
    
    
    
    ## Compruebo cantidad de parametros
    if len(argumentos) > 1:
        print("Cantidad de parametros incorrecta")
        exit()
        
    
    ## Si se ingreso un parametro lo paso como nombre para importar
    nombreArchivoJson = "questions.json"
    if len(argumentos) > 0:
        nombreArchivoJson = argumentos[0]


    ## importo el archivo y creo la variable
    print()
    print(f"IMPORTANDO ARCHIVO '{nombreArchivoJson}'")
    try:
        with open(nombreArchivoJson) as f:
            questions_json = json.load(f)
    except FileNotFoundError:
        print(f"El archivo '{nombreArchivoJson}' no existe en este directorio")
        exit()



    # configurar entorno de django
    print()
    print("CONFIGURANDO ENTORNO DE DJANGO")
    import django, os
    os.environ["DJANGO_SETTINGS_MODULE"] = "proyecto_iwg101.settings"
    django.setup()
    print("ENTORNO DE DJANGO CONFIGURADO CORRECTAMENTE")



    print()
    print("IMPORTANDO TABLAS DE LA BASE DE DATOS")
    # Modelos a usar
    from page.models import Area, Test, Pregunta
    print("TABLAS IMPORTADAS CORRECTAMENTE")



    print()
    print("INICIANDO CREACION DE PREGUNTAS")
    for question in questions_json:
        if not Area.objects.filter(nombre=question['area']).exists():
            print()
            print(f"EL AREA {question['area']} NO EXISTIA, CREANDO ESA AREA")
            Area(nombre=question['area']).save()
            print(f"AREA {question['area']} CREADA EXITOSAMENTE")
        if not Test.objects.filter(nombre=question['test']).exists():
            print()
            print(f"EL TEST {question['test']} NO EXISTIA, CREANDO ESE TEST")
            Test(nombre=question['test']).save()
            print(f"TEST {question['test']} CREADO EXITOSAMENTE")
        if not Pregunta.objects.filter(texto=question['texto']).exists():
            print()
            print(f"CREANDO PREGUNTA {question['texto']}")
            pregunta = Pregunta(texto=question['texto'],area=Area.objects.get(nombre=question['area']),test=Test.objects.get(nombre=question['test']))
            pregunta.save()
            print(f"PREGUNTA '{question['texto']}' CREADA EXITOSAMENTE")
        else:
            print()
            print(f"LA PREGUNTA '{question['texto']}' YA EXISTIA")