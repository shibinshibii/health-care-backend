from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    specialization = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='patient_mappings')

    class Meta:
        unique_together = ('patient', 'doctor')

