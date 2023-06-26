from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

# def inicio(request):
#     return HttpResponse('Hola soy tu inicio')

# V2
def inicio(request):
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

def segunda_vista(request):
    return HttpResponse('<h1> Soy la segunda vista</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha}')

def saludar(request):
    return HttpResponse('bienvenido')

def saludos(request, nombre, apellido):
    return HttpResponse(f'Bienvenido {nombre.title()} {apellido.title()}')