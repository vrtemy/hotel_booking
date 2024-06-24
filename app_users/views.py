from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import auth, messages

from app_users.forms import *
from app_users.services import *
from app_users.models import BookingRoom


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'app_users/registration.html', context)


def delete_order(request):
    if request.method == 'GET':
        pk = request.GET['pk']
        delete_order_room(BookingRoom, pk)
        messages.success(request, 'Бронь отменена.')

    return HttpResponseRedirect(reverse('user:profile'))


def profile(request):
    user_book_rooms = get_booking_rooms(BookingRoom, request.user.username)

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения применены!')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Личный кабинет',
        'form': form,
        'data': user_book_rooms
    }
    return render(request, 'app_users/user-page.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('hotel:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'app_users/authentication.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('hotel:index'))


def room_data_for_booking(request):
    data = request.POST
    
    request.session['room-data'] = data
    request.session.modified = True

    return redirect('user:booking')


def booking(request):
    data = request.session.get('room-data')

    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booked_room = BookingRoom(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                date_entry = request.POST['date_entry'],
                date_exit = request.POST['date_exit'],
                room_name = data['room_name'],
                price = data['price'],
                user = request.POST['username']
            )
            booked_room.save()
            messages.success(request, 'Номер забронирован! Проверьте личный кабинет')
            return HttpResponseRedirect(reverse('user:booking'))
    else:
        form = BookingForm()

    context = {
        'title': 'Бронируйте здесь',
        'form': form,
        'data': data
    }
    return render(request, 'app_users/booking.html', context)
