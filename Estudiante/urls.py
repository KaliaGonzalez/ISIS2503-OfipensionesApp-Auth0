from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('estudiantes/', views.estudiante_list, name='estudianteList'),
    path('estudiante/<id>', views.single_estudiante, name='singleEstudiante'),
    path('estudiantecreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
]
