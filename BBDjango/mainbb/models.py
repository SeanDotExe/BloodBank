from django.db import models
from django.db.models import aggregates

# Create your models here.
class reg_donor_patient(models.Model):
    bloodtype = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),
    ]
    sex=[

        ('M','Male'),
        ('F', 'Female')

    ]
    username = models.CharField(max_length=50)
    pword = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    add = models.CharField(max_length=200)
    age=models.DecimalField(max_digits=3,decimal_places=0)
    bloodtype = models.CharField(max_length=4,choices=bloodtype)
    sex = models.CharField(max_length=10,choices=sex)
    contactnum = models.DecimalField(max_digits=11,decimal_places=0)

