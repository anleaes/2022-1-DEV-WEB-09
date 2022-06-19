from distutils.archive_util import make_archive
from django.db import models

# Create your models here.

class Paciente_prontuario(models.Model):
    cpf = models.CharField(max_length=11, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    idade = models.IntegerField
    celular = models.CharField(max_length=12, null=False, blank=False)
    cid = models.IntegerField
    
class Medico(models.Model):
    crm = models.IntegerField
    nome = models.CharField(max_length=200, null=False, blank=False)
    celular = models.CharField(max_length=12, null=False, blank=False)
    especialidade = models.CharField(max_length=100, null=False, blank=False)

class enfermeiro(models.Model):
    nome = models.CharField(max_length=155, null=False, blank=False)
    celular = models.CharField(max_length=12, null=False, blank=False)