from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient, Doctor, Appointment, Room, RoomAllocation # Import your models

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Room)
admin.site.register(RoomAllocation)
# admin.site.register(payment)  # Ensure the Payment model is correctly defined in models.py
#     patient = models.ForeignKey('Patient', on_delete=models.CASCADE)