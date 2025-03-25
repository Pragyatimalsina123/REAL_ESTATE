from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Property(models.Model):
    HOUSE = 'house'
    APARTMENT = 'apartment'
    COMMERCIAL = 'commercial'

    PROPERTY_TYPES = [
        (HOUSE, 'House'),
        (APARTMENT, 'Apartment'),
        (COMMERCIAL, 'Commercial'),
    ]

    AVAILABLE = 'available'
    RENTED = 'rented'
    SOLD = 'sold'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (RENTED, 'Rented'),
        (SOLD, 'Sold'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default=HOUSE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=AVAILABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each property to a user

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            # Resize the image if it is too large
            max_size = (300, 200)
            img.thumbnail(max_size)
            img.save(self.image.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.property.title}'

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.user.username} - {self.property.title}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_properties = models.ManyToManyField(Property, related_name="favorited_by")

    def __str__(self):
        return self.user.username


# Signal to create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create UserProfile instance when User is created
        UserProfile.objects.create(user=instance)

# Signal to save UserProfile after the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Check if the User has a profile, if not, create it
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    else:
        UserProfile.objects.create(user=instance)
