from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/<int:id>', views.tests),
    path('resultados/', views.resultados),
    ## path('signin/', pendiente),
    ## path('signup/', pendiente),
    path('about/', views.about),
]
