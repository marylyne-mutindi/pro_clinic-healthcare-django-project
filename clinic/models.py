from datetime import date
from django.db import models
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    file = models.FileField(upload_to='patient_files/', null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def __str__(self):
        return self.name
# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)  # e.g., ICU, General, Private

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class RoomAllocation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    allocation_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient} assigned to {self.room} by Dr. {self.doctor.user.get_full_name()}"

class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100)
    dob = models.DateField()
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    details = models.TextField(blank=True)  # Doctor's bio or other details
    address = models.TextField()
    file = models.FileField(upload_to='doctor_files/', null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
    
class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=20)  # e.g., "10:00 AM - 10:30 AM"
    token_number = models.PositiveIntegerField()
    problem = models.TextField()

    def __str__(self):
        return f"Appointment #{self.token_number} - {self.patient.name} with Dr. {self.doctor.name} on {self.appointment_date}"
    
    
    class Payment(models.Model):
        patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
        department = models.CharField(max_length=100)
        doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
        admission_date = models.DateField()
        discharge_date = models.DateField(null=True, blank=True)
        service_name = models.CharField(max_length=100)
        cost_of_treatment = models.DecimalField(max_digits=10, decimal_places=2)
        advance_paid = models.DecimalField(max_digits=10, decimal_places=2)
        payment_method = models.CharField(max_length=50)  # e.g., Cash, Card, Check
        card_or_check_no = models.CharField(max_length=50, null=True, blank=True)
        payment_date = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f"Payment by {self.patient.name} for {self.service_name} - {self.payment_method}"