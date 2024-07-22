# core/admin.py
from django.contrib import admin
from .models import Profile, Listing  # Comment out Message

admin.site.register(Profile)
admin.site.register(Listing)
# admin.site.register(Message)  # Comment out or remove this line
