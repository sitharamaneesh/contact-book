from django.contrib import admin
from .models import contact

class ContactAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(contact,ContactAdmin)
# Register your models here.
