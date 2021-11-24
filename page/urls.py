from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('test/<int:id>', views.tests, name='tests'),
    path('resultados/', views.resultados, name='results'),
    path('about/', views.about, name='about'),
    path('procesar_preguntas/', views.procesar_preguntas, name='procesar_preguntas'),
    path('register/', views.register, name='register')
]
