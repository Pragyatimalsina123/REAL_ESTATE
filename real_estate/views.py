# real_estate/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


# View for the property listings page
def property_list(request):
    # Logic to fetch properties from the database can go here
    return render(request, 'property_list.html')  # Rendering the 'property_list.html' template

# View for the contact page
def contact(request):
    return render(request, 'contact.html')  # Rendering the 'contact.html' template

def services(request):
    return render(request, 'services.html')

def web_development(request):
    return render(request, 'web_development.html')  # Create this template as a detailed page

def mobile_app_development(request):
    return render(request, 'mobile_app_development.html') 

def seo_services(request):
    # This should render a template specific to SEO services
    return render(request, 'seo_services.html')

def digital_marketing(request):
    # This should render a template specific to Digital Marketing services
    return render(request, 'digital_marketing.html')

def graphic_design(request):
    # This should render a template specific to Graphic Design services
    return render(request, 'graphic_design.html')

def consulting_services(request):
    # This should render a template specific to Consulting services
    return render(request, 'consulting_services.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html') 