from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Curso(models.Model):
    curso = models.CharField(max_length=50)
    comision = models.CharField(max_length=50)

class Profes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)