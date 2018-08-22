from django.contrib import admin

# Register your models here.
from .models import Pet

@admin.regisiter(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
