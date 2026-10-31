from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Project
from .forms import ProjectForm

@login_required
def home(request):
    name = "Kevin"
    course = "TY BSc.IT"
    tagline = "Python Developer · Django Enthusiast · Tech Lover"

    skills = [
        {"name": "Python", "level": 85},
        {"name": "Django", "level": 75},
        {"name": "HTML & CSS", "level": 90},
        {"name": "JavaScript", "level": 60},
    ]

    tech_stack = [
        "Python", "Django", "HTML5", "CSS3",
        "JavaScript", "Git", "SQL", "Bootstrap",
    ]

    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
    else:
        projects = Project.objects.none()

    return render(request, 'home/home.html', {
        'name': name,
        'course': course,
        'tagline': tagline,
        'skills': skills,
        'tech_stack': tech_stack,
        'projects': projects,
    })


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            return render(request, 'home/add_project.html', {
                'form': ProjectForm(),
                'message': 'Project added successfully!'
            })

    else:
        form = ProjectForm()

    return render(request, 'home/add_project.html', {'form': form})


@login_required
def edit_project(request, id):

    project = get_object_or_404(
        Project,
        id=id,
        owner=request.user
    )

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()

            return render(request, 'home/edit_project.html', {
                'form': ProjectForm(instance=project),
                'message': 'Project updated successfully!'
            })

    else:
        form = ProjectForm(instance=project)

    return render(request, 'home/edit_project.html', {
        'form': form
    })
@login_required
def delete_project(request, id):

    project = get_object_or_404(
        Project,
        id=id,
        owner=request.user
    )

    if request.method == 'POST':
        project.delete()
        return redirect('home')

    return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'home/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'home/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'home/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')