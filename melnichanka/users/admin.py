from django.contrib import admin

from .models import CustomUser, Department, Position

admin.site.register(CustomUser)


admin.site.register(Department)
admin.site.register(Position)
