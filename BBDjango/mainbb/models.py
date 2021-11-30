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

        ('Male','Male'),
        ('Female', 'Female')

    ]

    username = models.CharField(max_length=50)
    pword = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    add = models.CharField(max_length=200)
    age=models.DecimalField(max_digits=3,decimal_places=0)
    bloodtype = models.CharField(max_length=4,choices=bloodtype)
    sex = models.CharField(max_length=10,choices=sex)
    contactnum = models.DecimalField(max_digits=11,decimal_places=0)

class add_reqdonate(models.Model):
    
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
        ('Male','Male'),
        ('Female', 'Female')
    ]
    choice=[
        ('Pending','Pending')
    ]
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    age=models.DecimalField(max_digits=3,decimal_places=0)
    sex = models.CharField(max_length=10,choices=sex)
    add = models.CharField(max_length=200)
    contactnum = models.DecimalField(max_digits=11,decimal_places=0)
    weight=models.DecimalField(max_digits=3,decimal_places=0)
    disease = models.CharField(max_length=100)
    unit=models.DecimalField(max_digits=3,decimal_places=0)
    bloodtype = models.CharField(max_length=4,choices=bloodtype)
    status = models.CharField(max_length=20, choices=choice)

class add_reqblood(models.Model):
    
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
        ('Male','Male'),
        ('Female', 'Female')
    ]
    choice=[
        ('Pending','Pending')
    ]
    username = models.CharField(max_length=50)
    patientname = models.CharField(max_length=100)
    patientage=models.DecimalField(max_digits=3,decimal_places=0)
    sex = models.CharField(max_length=10,choices=sex)
    healthfac = models.CharField(max_length=200)
    healthfacadd = models.CharField(max_length=200)
    contactnum = models.DecimalField(max_digits=11,decimal_places=0)
    disease = models.CharField(max_length=100)
    unit=models.DecimalField(max_digits=3,decimal_places=0)
    bloodtype = models.CharField(max_length=4,choices=bloodtype)
    status = models.CharField(max_length=20, choices=choice)
