from django.contrib import admin

# Register your models here.
from .models import UserProfile, Topping, Restaurant, Pizza

admin.site.register(UserProfile)
admin.site.register(Topping)
admin.site.register(Restaurant)
admin.site.register(Pizza)