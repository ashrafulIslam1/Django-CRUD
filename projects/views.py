from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):

    data = Project.objects.all()
    context = {'projects':data}

    return render(request, 'pages/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tag.all()
    return render(request, 'pages/single-project.html', {'project':projectobj, 'tag':tags})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context= {'form':form}
    return render(request, "pages/project-form.html", context)



def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = { 'form': form }
    return render(request, "pages/project-form.html", context)



def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = { 'object' : project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, "pages/delete-project.html", context)