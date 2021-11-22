from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('test/<int:id>', views.tests, name='tests'),
    path('resultados/', views.resultados, name='results'),
    ## path('signin/', pendiente, name='signin'),
    ## path('signup/', pendiente, name='signup'),
    path('about/', views.about, name='about'),
    path('procesar_preguntas/', views.procesar, name='procesar'),
]
