from django.contrib import admin
from .models import Pizza, Size
# Register your models here.

admin.site.register((Pizza, Size))