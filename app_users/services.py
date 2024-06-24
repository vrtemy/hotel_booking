from app_users.models import *


def get_booking_rooms(model, user):
    user_book_rooms = model.objects.all().filter(user=user)
    return user_book_rooms


def delete_order_room(model, pk):
    room_for_delete = model.objects.get(pk=pk)
    room_for_delete.delete()
