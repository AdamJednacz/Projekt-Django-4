from django.shortcuts import render, redirect,get_object_or_404
from .models import Project
from .forms import ProjectForm

def index(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')   
    else:
        form = ProjectForm()
        projects_list = Project.objects.all()
    return render(request, 'www/index.html', {'project_form': form,'projects_list':projects_list})



def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    return render(request, 'www/project_detail.html', {'project': project})
