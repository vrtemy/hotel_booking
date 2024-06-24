from django.db import models
from django.contrib.auth.models import AbstractUser

from app_hotel.models import HotelRoom


class BookingRoom(models.Model):
    """ Забронированный номер """
    first_name = models.CharField(max_length=200, default='Unknown')
    last_name = models.CharField(max_length=200, default='Unknown')
    date_entry = models.CharField(max_length=15)
    date_exit = models.CharField(max_length=15)
    room_name = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=10)
    user = models.CharField(max_length=200, default='Unknown')

    def __str__(self):
        return f'{self.room_name} | Вьезд: {self.date_entry} Выезд: {self.date_exit}'
    

class User(AbstractUser):
    """ Зарегистрированные пользователи """
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)
    


