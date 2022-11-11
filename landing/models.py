from django.contrib.auth.models import User
from django.db import models


class OldageHome(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo")
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.TextField()
    description = models.TextField()
    license_no = models.CharField(max_length=50)
    webaddress = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    oldageHome = models.ForeignKey(OldageHome, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=15)
    doctor_registration_no = models.CharField(max_length=50)
    specialized = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    oldageHome = models.ForeignKey(OldageHome, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    identification_number = models.CharField(max_length=50)
    address = models.TextField()
    highest_level_of_education = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'


class Site(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo")
    icon = models.ImageField(upload_to="logo")
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.TextField()


class Patient(models.Model):
    oldagehome = models.ForeignKey(OldageHome, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to="patient")
    guardian_phone_number = models.CharField(max_length=15, blank=True)
    guardian_nid = models.CharField(max_length=18, blank=True)

    def __str__(self):
        return f'{self.name}'


class Illness(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    disease_status = models.TextField()
    treatment_status = models.TextField()
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Donation(models.Model):
    nid = models.CharField(max_length=20)
    amount = models.IntegerField()
    message = models.TextField(blank=True)
    trx_id = models.CharField(max_length=100, primary_key=True)
