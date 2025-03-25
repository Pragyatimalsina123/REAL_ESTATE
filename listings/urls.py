from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import add_to_favorites


urlpatterns = [
    path('', views.property_list, name='property_list'),  # URL for listing all properties
    path('add/', views.property_add, name='property_add'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search_view, name='search'),
    path('wishlist/', views.wishlist_view, name='wishlist'), 
    path('add-to-favorites/<int:property_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add-to-wishlist/<int:property_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('listings/<int:pk>/', views.property_detail, name='property_detail'),
    path('<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', views.register, name='register'),  # Register URL (create a view for registration)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='listings/login.html'), name='login'),
]
