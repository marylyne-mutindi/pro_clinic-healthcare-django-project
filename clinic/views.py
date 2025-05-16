from django.shortcuts import redirect, render

from clinic.models import Patient

# Create your views here.
def patient_create(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        Patient.objects.create(
            patient_name=patient_name,
            dob=dob,
            gender=gender,
            phone=phone,
            email=email,
            image=image
        )
        return redirect('patient_list')

    return render(request, 'clinic/patient_form.html')

from .models import Doctor

def create_doctor(request):
    if request.method == 'POST':
        Doctor.objects.create(
            doctor_name=request.POST.get('doctor_name'),
            dob=request.POST.get('dob'),
            specialization=request.POST.get('specialization'),
            experience=request.POST.get('experience'),
            age=request.POST.get('age'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            gender=request.POST.get('gender'),
            doctor_details=request.POST.get('doctor_details'),
            address=request.POST.get('address'),
            file=request.FILES.get('file')
        )
        return redirect('doctor_list')
    return render(request, 'clinic/doctor_form.html')

from .models import Appointment

def create_appointment(request):
    if request.method == 'POST':
        Appointment.objects.create(
            patient_id=request.POST.get('patient_id'),
            department=request.POST.get('department'),
            doctor_name=request.POST.get('doctor_name'),
            appointment_date=request.POST.get('appointment_date'),
            time_slot=request.POST.get('time_slot'),
            token_number=request.POST.get('token_number'),
            problem=request.POST.get('problem')
        )
        return redirect('appointment_list')
    return render(request, 'clinic/appointment_form.html')

from .models import RoomAllocation

def create_room_allocation(request):
    if request.method == 'POST':
        RoomAllocation.objects.create(
            room_number=request.POST.get('room_number'),
            room_type=request.POST.get('room_type'),
            patient_name=request.POST.get('patient_name'),
            allocation_date=request.POST.get('allocation_date'),
            discharge_date=request.POST.get('discharge_date'),
            doctor_name=request.POST.get('doctor_name')
        )
        return redirect('room_allocation_list')
    #return render  It displays an HTML page by rendering a template with context (data).when to use it: When you want to show a page to the user.For example: Displaying a form, showing a list of patients, etc.
    return render(request, 'clinic/room_allocation_form.html') 

# from .models import Payment

# def create_payment(request):
#     if request.method == 'POST':
#         Payment.objects.create(
#             patient_name=request.POST.get('patient_name'),
#             amount=request.POST.get('amount'),
#             payment_method=request.POST.get('payment_method'),
#             payment_date=request.POST.get('payment_date')
#         )
#         return redirect('payment_list')
#     return render(request, 'clinic/payment_form.html')


