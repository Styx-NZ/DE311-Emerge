from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    shelf = Project.objects.all()
    return render(request, 'emerge/home.html', {'shelf': shelf})

def index(request):
    shelf = Project.objects.all()
    return render(request, 'emerge/emerge.html', {'shelf': shelf})

def about(request):
    shelf = Project.objects.all()
    return render(request, 'emerge/about.html', {'shelf': shelf})


def upload(request):
    upload = ProjectCreate()
    if request.method == 'POST':
        upload = ProjectCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('emerge')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'emerge'}}">reload</a>""")
    else:
        return render(request, 'emerge/upload_form.html', {'upload_form':upload})


def update_project(request, project_id):
    project_id = int(project_id)
    try:
        project_sel = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        return redirect('emerge')
    project_form = ProjectCreate(request.POST or None, instance = project_sel)
    if project_form.is_valid():
       project_form.save()
       return redirect('emerge')
    return render(request, 'emerge/upload_form.html', {'upload_form':project_form})


def delete_project(request, project_id):
    project_id = int(project_id)
    try:
        project_sel = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        return redirect('emerge')
    project_sel.delete()
    return redirect('emerge')
