from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from .models import Favorite, Property
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Property, Favorite,Wishlist
from django.contrib.auth.forms import UserCreationForm

def search_view(request):
    # Handle the search logic here
    query = request.GET.get('q')  # Example of getting a search query from GET parameters
    # You can add logic to search properties or whatever content you're searching
    return render(request, 'listings/search_results.html', {'query': query})

def favorites(request):
    # Assuming you have a model for properties and users can mark favorites
    user_favorites = request.user.favorite_properties.all()  # Modify this according to your model
    return render(request, 'listings/favorites.html', {'favorites': user_favorites})

def wishlist_view(request):
    # Handle logic for displaying wishlist
    return render(request, 'listings/wishlist.html')

@login_required
def add_to_favorites(request):
    if request.method == 'POST':
        # Get property ID from the POST request
        property_id = request.POST.get('propertyId')

        try:
            property = Property.objects.get(id=property_id)

            # Check if the property is already in the user's favorites
            if Favorite.objects.filter(user=request.user, property=property).exists():
                messages.info(request, 'This property is already in your favorites.')
                return JsonResponse({'success': False, 'message': 'Already added to favorites'})

            # Add to favorites
            Favorite.objects.create(user=request.user, property=property)
            messages.success(request, 'Property added to favorites!')
            return JsonResponse({'success': True, 'message': 'Property added to favorites!'})

        except Property.DoesNotExist:
            messages.error(request, 'Property not found.')
            return JsonResponse({'success': False, 'message': 'Property not found'})

    messages.error(request, 'Invalid request method.')
    return JsonResponse({'success': False, 'message': 'Invalid request method'})


       
# Add a new property (only accessible by authenticated users)
@login_required
def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user  # Set the current logged-in user as the owner
            property.save()
            return redirect('property_list')  # Redirect to the property list after saving
    else:
        form = PropertyForm()

    return render(request, 'listings/property_add.html', {'form': form})


# Edit an existing property (only accessible by the property owner or admin)
@login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)

    # Try loading the template manually
    try:
        get_template('property_edit.html')
    except TemplateDoesNotExist:
        print("Template does not exist")
    else:
        print("Template found")

    # Your existing code
    if request.user != property.user and not request.user.is_superuser:
        return redirect('property_list')  # Redirect to the list if not the owner or admin

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=property.pk)  # Redirect to the property detail page
    else:
        form = PropertyForm(instance=property)

    return render(request, 'listings/property_edit.html', {'form': form, 'property': property})


# Delete a property (only accessible by the property owner or admin)
@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)

    # Check if the logged-in user is the owner of the property or an admin
    if request.user != property.user and not request.user.is_superuser:
        return redirect('property_list')  # Redirect to the list if not the owner or admin

    if request.method == 'POST':
        property.delete()  # Delete the property from the database
        return redirect('property_list')  # Redirect to the property list after deletion

    return render(request, 'property_confirm_delete.html', {'property': property})


# Property detail view - Display property information
def property_detail(request, pk):
    # Get the property by its primary key (ID)
    property = get_object_or_404(Property, pk=pk)
    
    # Check if the property is already in the user's favorites
    is_favorite = False
    if request.user.is_authenticated:
        # Check if the property is already in the user's favorites
        is_favorite = Favorite.objects.filter(user=request.user, property=property).exists()

    # Pass the property and whether it's a favorite to the template
    return render(request, 'listings/property_detail.html', {
        'property': property,
        'is_favorite': is_favorite,  # Add this flag to indicate if it's a favorite
    })


# List all properties
def property_list(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'listings/property_list.html', {'properties': properties})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create the new user
            form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = UserCreationForm()
    
    return render(request, 'listings/register.html', {'form': form})

@login_required
def add_to_wishlist(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if Wishlist.objects.filter(user=request.user, property=property).exists():
        messages.info(request, 'This property is already in your wishlist.')
        return JsonResponse({'success': False, 'message': 'Already added to wishlist'})

    Wishlist.objects.create(user=request.user, property=property)
    messages.success(request, 'Property added to wishlist')
    return JsonResponse({'success': True, 'message': 'Property added to wishlist'})

@login_required
def wishlist(request):
    user_wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': user_wishlist})

