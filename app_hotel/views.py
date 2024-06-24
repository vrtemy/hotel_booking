from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from app_hotel.services import *


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'app_hotel/index.html', context)


def about_us(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'app_hotel/about-us.html', context)


def gallery(request):
    context = {
        'title': 'Галлерея',
        'hotel_rooms': all_objects(HotelRoom)
    }
    return render(request, 'app_hotel/gallery.html', context)


