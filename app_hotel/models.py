from django.db import models


class HotelRoom(models.Model):
    """ Таблица с номерами в отеле и информацией о них """
    name = models.CharField(max_length=200)
    count_rooms = models.PositiveIntegerField(default=1)
    max_guests = models.PositiveIntegerField(default=1)
    child_place = models.BooleanField(default=False)
    price_pn = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rooms_images')
    description = models.TextField(null=True, blank=True)
    booked_now = models.BooleanField(default=False)

    def __str__(self):
        return f'НАЗВАНИЕ: {self.name} | ЦЕНА (За ночь): {self.price_pn}'
