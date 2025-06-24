from django.contrib import admin
from .models import Appointment, Contact, Doctor

admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Doctor)
