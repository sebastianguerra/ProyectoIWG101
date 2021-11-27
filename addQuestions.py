#!/usr/bin/env python3
import json

# configurar entorno de django
import django, os
os.environ["DJANGO_SETTINGS_MODULE"] = "proyecto_iwg101.settings"
django.setup()

# Modelos a usar
from page.models import Area, Test, Pregunta



with open("questions.json") as f:
    questions_json = json.load(f)


for question in questions_json:
    if not Area.objects.filter(nombre=question['area']).exists():
        Area(nombre=question['area']).save()
    if not Test.objects.filter(nombre=question['test']).exists():
        Test(nombre=question['test']).save()
    if not Pregunta.objects.filter(texto=question['texto']).exists():
        pregunta = Pregunta(texto=question['texto'],area=Area.objects.get(nombre=question['area']),test=Test.objects.get(nombre=question['test']))
        pregunta.save()