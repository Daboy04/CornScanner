from django.contrib import admin
from .models import User


@admin.register(User)
class Admin(admin.ModelAdmin):
    search_fields = ('id', 'first_name','last_name','email')
    list_display = ('id', 'first_name','last_name','email')
