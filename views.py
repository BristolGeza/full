from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Project
from .forms import ProjectForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return JsonResponse({'success': True})
