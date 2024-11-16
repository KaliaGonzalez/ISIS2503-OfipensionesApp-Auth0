from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import EstudianteForm
from .logic.variable_logic import get_estudiantes, get_estudiante, create_estudiante
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
#from monitoring.auth0backend import getRole

@login_required
def estudiante_list(request):
    role = getRole(request)
    if role == "Administrador":
        estudiantes = get_estudiantes()
        context = {
            'estudiante_list': estudiantes
        }
        return render(request, 'Estudiante/estudiantes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_estudiante(request, id=0):
    estudiante = get_estudiante(id)
    context = {
        'estudiante': estudiante
    }
    return render(request, 'Estudiante/estudiante.html', context)

@login_required
def estudiante_create(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            form = EstudianteForm(request.POST)
            if form.is_valid():
                create_estudiante(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created student')
                return HttpResponseRedirect(reverse('estudianteCreate'))
            else:
                print(form.errors)
        else:
            form = EstudianteForm()

        context = {
            'form': form,
        }
        return render(request, 'Estudiante/estudianteCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
