from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Projects
from .forms import ProjectForm

def get_projects(request):
    """
    Create view with all existing Projects, which exist before now,
    render them to the projects.html template
    """
    # Filter projects by published_date
    projects = Projects.objects.filter(published_date__lte=timezone.now()
                                        ).order_by('-published_date')
    return render(request, "projects.html", {"projects": projects})



def project_details(request, pk):
    """
    Creat view returning a Project object referenced by its PrimaryKey/ID,
    render the Project details to projectdetails.html.
    Return a 404 if Project is not found.
    """
    #
    project = get_object_or_404(Projects, pk=pk)
    project.views += 1
    project.save()
    return render(request, "projectdetails.html", {"post": post})

def create_or_edit_project(request, pk=None):
    """
    Create view that can either create or edit a Project, 
    edits if exists or creates if not. 
    """