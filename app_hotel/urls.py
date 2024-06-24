from django.urls import path

from app_hotel.views import *

app_name = 'app_hotel'

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('gallery/', gallery, name='gallery')
]
