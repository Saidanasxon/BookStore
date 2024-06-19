from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('seller', 'Seller')
    )
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/l60Hf.png')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='client')


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username