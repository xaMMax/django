from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Reference to the Django User model
    phone_number = models.CharField(max_length=12, unique=True)  # User's phone number
    bio = models.TextField(blank=True)  # Short profile description (optional)

    def __str__(self):
        return str(self.user)  # Return the string representation of the user


# Create a user profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Save the user profile when user data is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()  # Save the user profile after saving user data
