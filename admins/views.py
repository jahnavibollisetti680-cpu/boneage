import os
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from users.models import UserRegistrationModel

# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        # TODO: Replace with proper authentication system
        admin_user = os.environ.get('ADMIN_USER', 'admin')
        admin_pass = os.environ.get('ADMIN_PASS', 'admin')
        if usrid == admin_user and pswd == admin_pass:
            request.session['admin_logged'] = True
            return render(request, 'admins/AdminHome.html')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/viewregisterusers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        UserRegistrationModel.objects.filter(id=uid).exclude(status__iexact='activated').update(status='activated')
        return redirect('RegisterUsersView')