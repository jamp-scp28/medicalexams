from django.db import models
from django.utils import timezone
from django.urls import reverse

from corecode.models import StudentClass, Subject
from django.core.validators import RegexValidator

class Employee(models.Model):
  STATUS = [
      ('activo', 'Activo'),
      ('inactivo', 'Inactivo')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  current_status        = models.CharField(max_length=10, choices=STATUS, default='activo',blank=True,null=True)
  date_of_birth         = models.DateField(default=timezone.now,verbose_name="Fecha Ingreso")
  registration_number   = models.CharField(max_length=200, unique=True, verbose_name="ID")
  Enterprise               = models.CharField(max_length=200,verbose_name="Empresa",blank=True)
  name               = models.CharField(max_length=200,verbose_name="Nombre",blank=True)

  #mobile_num_regex      = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  #parent_mobile_number  = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)

  department               = models.CharField(max_length=300,verbose_name="Departamento",blank=True)
  job_name                = models.CharField(max_length=300,verbose_name="Cargo",blank=True)
  #passport              = models.ImageField(blank=True, upload_to='students/passports/')  

  class Meta:
    ordering = ['name']

  def __str__(self):
    return f'{self.name}  - {self.department}'

  def get_absolute_url(self):
    return reverse('employee-detail', kwargs={'pk': self.pk})


class StudentBulkUpload(models.Model):
  date_uploaded       = models.DateTimeField(auto_now=True)
  csv_file            = models.FileField(upload_to='students/bulkupload/')
