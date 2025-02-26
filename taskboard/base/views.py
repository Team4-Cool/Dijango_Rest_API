from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, User

@login_required
def home(request):
    return render(request, 'base/home.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please fill all fields!')
            return redirect('login')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password!')
            return redirect('login')

    return render(request, 'login.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not first_name or not last_name or not email or not password:
            messages.error(request, 'Please fill all fields!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'register.html')


def board(request):
    tasks = Task.objects.all()
    todo_tasks = tasks.filter(status='TASK')
    in_progress_tasks = tasks.filter(status='IN_PROGRESS')
    in_review_tasks = tasks.filter(status='IN_REVIEW')
    done_tasks = tasks.filter(status='DONE')

    context = {
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'in_review_tasks': in_review_tasks,
        'done_tasks': done_tasks,
    }
    return render(request, 'board.html', context)


def roles(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page!')
        return redirect('home')

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_role = request.POST.get('role')

        try:
            user = User.objects.get(id=user_id)
            user.role = new_role
            user.save()
            messages.success(request, f'Role updated for {user.email}!')
        except User.DoesNotExist:
            messages.error(request, 'User not found!')

    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'manage_roles.html', context)