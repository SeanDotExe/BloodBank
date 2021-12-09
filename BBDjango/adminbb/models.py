from django.db import models
from django.db.models import aggregates

# Create your models here.
class reg_admin(models.Model):
    prof = [
        ('Medical Technologist','Medical Technologist'),
        ('Physician','Physician'),
        ('Nurse','Nurse'),
    ]
    sex=[

        ('Male','Male'),
        ('Female', 'Female')

    ]

    username = models.CharField(max_length=50)
    pword = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    profession = models.CharField(max_length=30,choices=prof)
    sex=models.CharField(max_length=6)
    contactnum = models.DecimalField(max_digits=11,decimal_places=0)

class blood_counter(models.Model):
    Apos = models.DecimalField(max_digits=9,decimal_places=0)
    Aneg = models.DecimalField(max_digits=9,decimal_places=0)
    Bpos = models.DecimalField(max_digits=9,decimal_places=0)
    Bneg = models.DecimalField(max_digits=9,decimal_places=0)
    ABpos = models.DecimalField(max_digits=9,decimal_places=0)
    ABneg = models.DecimalField(max_digits=9,decimal_places=0)
    Opos = models.DecimalField(max_digits=9,decimal_places=0)
    Oneg = models.DecimalField(max_digits=9,decimal_places=0)