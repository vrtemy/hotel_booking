from django.contrib import admin

from app_users.models import User, BookingRoom

admin.site.register(User)
admin.site.register(BookingRoom)