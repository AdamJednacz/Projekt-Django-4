from django.shortcuts import render, redirect,get_object_or_404
from .models import Project,Task,Done
from .forms import ProjectForm,TaskForm

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
    task_list = Task.objects.filter(project=project)  # Filter tasks for this project only
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save to database yet
            task.project = project  # Associate task with the current project
            task.save()  # Now save to the database
            return redirect('project_detail', project_id=project.id)  # Pass the project_id to the redirect
    else:
        form = TaskForm()
       
    return render(request, 'www/project_detail.html', {'task_form': form, 'project': project, 'task_list': task_list})


def done(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        project_id = task.project.id  # Get the project ID associated with the task
        done, created = Done.objects.get_or_create(task=task)
        if not created:
            done.delete()
        return redirect('project_detail', project_id=project_id)