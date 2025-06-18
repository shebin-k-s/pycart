from django.db import IntegrityError
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer
from django.contrib.auth.decorators import login_required


@login_required(login_url='account')
def profile(request):

    user = request.user

    print(user)

    profile = user.profile

    print(profile)
    return render(request, 'profile.html', {'profile': profile})


def account_view(request):
    if 'next' in request.GET:
        messages.warning(request, "You must log in to continue.")

    register = False
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if 'register' in request.POST:
            register = True
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )

                user.save()

                if user:
                    customer = Customer.objects.create(
                        user=user,
                        address=address,
                        phone=phone
                    )

                messages.success(request, "User Registered")
            except IntegrityError:
                messages.error(request, "Username or email already exists.")
            except Exception as e:
                messages.error(request, f"Something went wrong: {e}")
        else:
            try:
                user = authenticate(
                    username=username, password=password)

                print(user)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "User not found")

            except Exception as e:
                error_message = e
                print(e)
                messages.error(request, error_message)

    return render(request, 'account.html', {'register': register})


def logout_user(request):
    logout(request)

    return redirect('account')
