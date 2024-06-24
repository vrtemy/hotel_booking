from django.urls import path

from app_users.views import *

app_name = 'app_hotel'

urlpatterns = [
    path('delete-order/', delete_order, name='delete_order'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('booking/', booking, name='booking'),
    path('room-data/', room_data_for_booking, name='room_data')
]
