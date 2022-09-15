from django.contrib import admin

from .models import Shoe, Reason

# Register your models here.

admin.site.register(Shoe)
admin.site.register(Reason)