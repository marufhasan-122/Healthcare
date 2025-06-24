from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                            # Home page with appointment form
    path('about/', views.about, name='about'),                    # About page
    path('services/', views.services, name='services'),           # Services page
    path('contact/', views.contact, name='contact'),              # Contact page (GET)
    path('contact/submit/', views.contact_form, name='contact_form'),  # Contact form POST handler
    path('appointment/', views.make_appointment, name='make_appointment'),  # POST-only fallback
    path('doctors/', views.doctor_list, name='doctors'),          # List of doctors
]
