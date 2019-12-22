from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from order.models import Order


def register(request):
    """ Register function that check user name and email is it unique """
    if request.method == 'POST':
        # Get values from registration form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if len(password) < 6:
            messages.error(request, 'Password too short - minimum 6 characters')
            return redirect('register')
        # Check passwords
        if password == password2:
            # Check username & email
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'That username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                # If everything pass, save user in database
                else:
                    user = User.objects.create_user(username=uname, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, ' Thank you for creating an account. You can now log in!')
                    return redirect('login')
            return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
        return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    """ Login user authentication """
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']

        user = auth.authenticate(username=uname, password=password)
        # If use in databse log in if not return a message
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Wrong password or/and login')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    """ Simple logout """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
    return redirect('index')


@login_required()
def dashboard(request):
    """ User dahsboard page """
    get_orders = Order.objects.filter(user=request.user.id)
    context = {
        'get_orders': get_orders,
    }
    return render(request, 'accounts/dashboard.html', context)
