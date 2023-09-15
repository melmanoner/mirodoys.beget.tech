from django.contrib import admin
from .models import Applications, Balance, Warehouse

# Register your models here.

admin.site.register(Applications)
admin.site.register(Balance)
admin.site.register(Warehouse)

