from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name}"

