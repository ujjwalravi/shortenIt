from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from . import shortener

# Create your views here.

@login_required(login_url='login')
def index(request):
    u = request.user
    datas = UrlShort.objects.filter(user=u)
    print(datas)
    tc = 0
    mc = -1
    for data in datas:
        tc = tc + data.visits
        if data.visits >  mc:
            mc = data.visits
    context = {'tc': tc, 'lu': len(datas), 'mc': mc}
    return render(request, 'urlshort/index.html', context)

@login_required(login_url='login')
def random(request):
    form = UrlShortForm()
    if request.method == 'POST':
        form = UrlShortForm(request.POST)
        to_update = form.save(commit=False)
        hashed = shortener.shortenIt()
        to_update.short = hashed
        to_update.user = request.user
        to_update.save()
        #return HttpResponse('Random Short Url generated!' + '<br>' + '<br>' + '<a href="http://127.0.0.1:8000/r/"')
        return render(request, 'urlshort/randomresponse.html', {'hashed': hashed})
    return render(request, 'urlshort/random.html', {'form': form})

@login_required(login_url='login')
def custom(request):
    form = CustomUrlForm()
    if request.method == 'POST':
        form = CustomUrlForm(request.POST)
        to_update = form.save(commit=False)
        to_update.user = request.user
        val = to_update.short
        to_update.save()
        return render(request, 'urlshort/customresponse.html', {'hashed': val})
    return render(request, 'urlshort/custom.html', {'form': form})

@login_required(login_url='login')
def edit(request, id):
    data = UrlShort.objects.get(id=id)
    form = UpdateUrlForm(instance=data)
    if request.method == 'POST':
        form = UpdateUrlForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'urlshort/updateUrl.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'urlshort/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'urlshort/relogin.html')
    return render(request, 'urlshort/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')

def shurl(request, u):
    if UrlShort.objects.filter(short=u).exists():
        link = UrlShort.objects.get(short=u)
        link.visits = link.visits+1
        link.save()
        return redirect(link.original)
    return HttpResponse('Corresponding URL NOT FOUND')

@login_required(login_url='login')
def dashboard(request):
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    print(request.META.get('REMOTE_ADDR'))
    #urlData = UrlShort.objects.order_by('-date_created')
    urlData = UrlShort.objects.filter(user=request.user).order_by('-date_created')
    context = {'data': urlData}
    return render(request, 'urlshort/dashboard.html', context)

@login_required(login_url='login')
def delete(request, id):
    UrlShort.objects.get(id=id).delete()
    return redirect('dashboard')
