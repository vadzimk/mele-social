from django.conf import settings
from django.db import models

# it is better to create custom user model form AbstractUser right away instead of this approach
class Profile(models.Model):
    #  https://docs.djangoproject.com/en/4.1/topics/ auth/customizing/#django.contrib.auth.get_user_model.
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)  # Pillow library is required

    def __str__(self):
        return f'Profile of {self.user.username}'
