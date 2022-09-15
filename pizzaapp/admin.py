from django.contrib import admin
from .models import Pizza, Size, Cart
# Register your models here.

admin.site.register((Pizza, Size, Cart))