from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponse, HttpResponseRedirect

from .models import Registration, Personnal, District, Branch, AccountType
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'Home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)

        else:
            return render(request, 'login.html',
                          {'message': "Username or password is incorrect"})

        return redirect('bankapp:success_page')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html',
                              {'message': "Username already exists."})
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                Registration.objects.create(username=username, password=password)
        else:

            return render(request, 'register.html', {'message': "Passwords do not match."})
        return redirect('bankapp:login')

    return render(request, 'register.html')


def register_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phonenumber = request.POST.get('phonenumber')
        mailid = request.POST.get('mailid')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        AccountType = request.POST.get('AccountType')
        materials_provide1 = request.POST.get('materials_provide1')
        materials_provide2 = request.POST.get('materials_provide1')
        materials_provide3 = request.POST.get('materials_provide3')
        return redirect('bankapp:submit_form')
    return render(request, 'register_form.html')


def submit_form(request):
    if request.method == 'POST':

        confirmation_message = 'Order Confirmed'
        return render(request, 'submit_form.html', {'confirmation_message': confirmation_message})
    else:
        return render(request, 'submit_form.html')


def success_page(request):
    return render(request, 'success_page.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
