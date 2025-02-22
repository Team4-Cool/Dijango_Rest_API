from rest_framework import viewsets
from .models import Task, Admin, User
from .serializers import UserSerializer, AdminSerializer, TaskSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


@login_required
def home(request):
    return render(request, 'base/home.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')  

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:  
            messages.error(request, 'Fields can`t be empty.')
            return redirect('/login/')
        
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Not right data.")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    
    return render(request, 'login.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not first_name or not last_name or not email or not password: 
            messages.error(request, "Fill all fields , it`s necessarily!")
            return redirect('/register/')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email is using!")
            return redirect('/register/')
        
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        messages.info(request, "Account created succsesfull!")
        return redirect('/login/')  

    return render(request, 'register.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
