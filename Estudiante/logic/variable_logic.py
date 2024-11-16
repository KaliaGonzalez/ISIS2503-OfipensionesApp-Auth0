from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_estudiante(id):
    estudiante = Estudiante.objects.raw("SELECT * FROM estudiantes_estudiante WHERE id=%s" % id)[0]
    return (estudiante)

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()
