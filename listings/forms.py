from django import forms
from .models import Property
from django.core.exceptions import ValidationError

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'address', 'city', 'state', 'zip_code', 'property_type', 'status', 'image']
        
    image = forms.ImageField(required=False)  # Image is optional, so it's not required

    # Validation for price field
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    # Custom validation for image field (optional but if provided, checks its validity)
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Optional: Check if the image file size is not too large (e.g., 5MB max)
            max_size = 5 * 1024 * 1024  # 5 MB
            if image.size > max_size:
                raise ValidationError("The image file is too large. Max size is 5MB.")
        return image
