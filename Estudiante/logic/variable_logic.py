from ..models import Estudiante
from django.core.exceptions import ObjectDoesNotExist

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

"""def get_estudiante(id):
    estudiante = Estudiante.objects.raw("SELECT * FROM Estudiante_estudiante WHERE id=%s" % id)[0]
    return (estudiante)""" 
def get_estudiante(id): 
    try: 
        estudiante = Estudiante.objects.get(id=id)
        return estudiante
    except ObjectDoesNotExist:
        return None

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()
