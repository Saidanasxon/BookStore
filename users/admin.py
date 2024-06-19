from django.contrib import admin
from .models import User, Seller, Client

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Client)