from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from EWMC.form import UsermessageForm, NattestForm
from nattest.models import Nattest
from schedule.models import Schedule
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'GET':
        context = {
            'form': UsermessageForm(),
        }
        return render(request, 'index.html', context, )
    else:
        form = UsermessageForm(request.POST)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.user_id = request.user.id
            mydata.save()
            messages.success(request, 'The form is valid.', extra_tags='alert')
            return redirect('index')
        else:
            messages.warning(request, 'The form is invalid.', extra_tags='alert')
        return render(request, 'index.html', {'form': form})


def applicationForm(request):
    if request.method == 'GET':
        context = {
            'appform': NattestForm(),
            'schedule': [Schedule.objects.latest("id")],
            'form': UsermessageForm(),
        }
        return render(request, 'nattest.html', context)
    else:
        form = NattestForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            mydata = form.save(commit=False)
            mydata.save()
            fl = mydata.firstname
            fn = mydata.firstname
            ln = mydata.lastname
            dob = mydata.dob
            email = mydata.email
            id = mydata.id
            html_content = "<h2 style='font-family: Garamond; font-size: 24px;font-weight: normal;'>Dear %s,<br> Your " \
                           "form is successfully submitted, Here is your details</h2> <br><h3 style='font-family: " \
                           "Garamond;font-size: 24px;font-weight: normal;'>registration id: %s <br> First Name: %s <br>" \
                           "Last Name: %s  <br> Date of Birth: %s </h3> " \
                           "......................................<br>NAT TEST Office (Kathmandu)<br>Chabahil - 7," \
                           "Kathmandu Nepal<br>Phone: 4482809"
            mail = EmailMessage(subject='Confirmation about NAT Test', body=html_content % (fl, id, fn, ln, dob),
                                to=[email])
            mail.content_subtype = 'html'
            mail.send()
            messages.success(request, 'The form is valid.', extra_tags='alert')
            return redirect('applicationForm')
        else:
            messages.warning(request, 'The form is invalid.', extra_tags='alert')
        return render(request, 'nattest.html', {'form': form})


def signin(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'login.html', context)
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('signin')


@login_required(login_url='signin')
def dashboard(request):
    context = {
        'nat': Nattest.objects.all(),
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='signin')
def confirm(request, id):
    data = Nattest.objects.get(pk=id)
    if data.role == 0:
        data.role = 1
        data.save()
    else:
        data.role = 0
        data.save()
    return redirect('dashboard')


@login_required(login_url='signin')
def my_logout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def details(request, id):
    context = {
        'nat': Nattest.objects.filter(pk=id),
    }
    return render(request, 'details.html', context)


@login_required(login_url='login')
def nattest_edit(request, id):
    data = Nattest.objects.get(pk=id)
    form = NattestForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'nattest_edit.html', context)


@login_required(login_url='login')
def nattest_delete(request, id):
    std = Nattest.objects.get(pk=id)
    std.delete()
    return redirect('dashboard')
