from django.contrib import admin
from .models import Studetn

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model=Studetn
        fields="__all__"
        
