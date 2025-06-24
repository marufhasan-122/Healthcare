from django.shortcuts import render, redirect
from .models import Appointment, Contact, Doctor
from django.contrib import messages
import datetime

def home(request):
    """Render the home page and handle appointment form."""
    if request.method == 'POST':
        # Handles the appointment form on home page
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = request.POST.get('date')

        if name and email and date:
            Appointment.objects.create(
                name=name,
                email=email,
                message=message,
                date=date
            )
            messages.success(request, "Your appointment has been submitted successfully.")
        else:
            messages.error(request, "Please fill all required fields.")
        return redirect('home')

    today = datetime.date.today().isoformat()
    return render(request, 'core/home.html', {'today_date': today})


def make_appointment(request):
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = request.POST.get('date')
        doctor_id = request.POST.get('doctor')

        if name and phone and date and doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            Appointment.objects.create(
                name=name,
                phone=phone,
                message=message,
                date=date,
                doctor=doctor
            )
            messages.success(request, "Appointment booked successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'core/appointment.html', {'doctors': doctors})


def contact_form(request):
    """Handle contact form submissions."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')
    return render(request, 'core/contact.html')


def about(request):
    """About page view."""
    return render(request, 'core/about.html')


def services(request):
    """Services page view with dynamic service data."""
    services = [
        ("Allergies", "Allergies can be treated with prescriptions.", "icon/allergy.jpg"),
        ("Cancer", "Cancer treatment requires diagnosis and care.", "icon/cancer.jpg"),
        ("Diabetes", "Doctors provide medication and guidance.", "icon/diabetes.jpg"),
    ]
    return render(request, 'core/services.html', {'services': services})


def doctor_list(request):
    """Render the list of doctors."""
    doctors = Doctor.objects.all()
    return render(request, 'core/doctors.html', {'doctors': doctors})


def contact(request):
    """Contact page GET request."""
    return render(request, 'core/contact.html')
