from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Estudiantes, Curso, Profes
from django.shortcuts import render


# V2
def prueba(request):
    # archivo = open(r'C:\Users\facun\Documents\Visual Studio Code\django_entregable\templates\index.html', 'r')
    # template = Template(archivo.read())
    template = loader.get_template("index.html")
    # archivo.close()
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'lista_numeros': list(range(25))
    }
    # contexto = Context(diccionario)
    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)

def inicio(request):
    return render(request, 'index.html')

def segunda_vista(request):
    return HttpResponse('<h1> Soy la segunda vista</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha}')

def saludar(request):
    return HttpResponse('bienvenido')

def saludos(request, nombre, apellido):
    return HttpResponse(f'Bienvenido {nombre.title()} {apellido.title()}')

def estudiantes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')

        estudiantes = Estudiantes(nombre=nombre, apellido=apellido)
        diccionario = {
        }
        return render(request, 'estudiantes.html', diccionario)

    return render(request, 'estudiantes.html')

def profes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')

        profes = Profes(nombre=nombre, apellido=apellido)
        diccionario = {
        }
        return render(request, 'estudiantes.html', diccionario)

    return render(request, 'estudiantes.html')


def cursoFormulario(request):
    if request.method == 'POST':
        curso = request.POST.get('nombre', '')
        comision = request.POST.get('apellido', '')

        perro = Curso(curso=curso, comision=comision)
        diccionario = {
            'perro': perro,
        }
        return render(request, 'crear_perro.html', diccionario)
    return render(request, "cursoFormulario.html")