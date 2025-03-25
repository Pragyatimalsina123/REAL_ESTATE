"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views
from .views import property_list, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls')),
    path('', RedirectView.as_view(url='/listings/', permanent=False)),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    
    # Service URLs
    path('services/web-development/', views.web_development, name='web_development'),
    path('services/mobile-app-development/', views.mobile_app_development, name='mobile_app_development'),
    path('services/seo-services/', views.seo_services, name='seo_services'),  # Add this for SEO Services
    path('services/digital-marketing/', views.digital_marketing, name='digital_marketing'),
    path('about/', views.about, name='about'),  # Add for Digital Marketing
    path('services/graphic-design/', views.graphic_design, name='graphic_design'),  # Add for Graphic Design
    path('services/consulting-services/', views.consulting_services, name='consulting_services'),  # Add for Consulting Services
    path('accounts/profile/', views.profile, name='profile'),

    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='listings/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
 # Include the Django auth URLs
    # Other app URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
