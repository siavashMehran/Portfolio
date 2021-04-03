from CVprojects.models import Categories, Project
from django.shortcuts import render
from django.http import Http404
# Create your views here.

def projects(request):
    
    projectList = Project.objects.get_all_active()
    categories  = Categories.objects.all()
    mostViewd   = Project.objects.get_most_viewd()[:3]
    context = {
        'list'  :  projectList,
        'categories' :  categories,
        'most_view' : mostViewd
    }
    return render(request, 'projects.html', context)




def projectDetailView(request, slug):

    project = Project.objects.getProjectbySlug(slug)
    project.viewsPlusOne()
    allTechs = project.get_project_techs()
        

    
    context = {
        'project'   : project,
        'techs' : allTechs
    }

    return render(request, 'projectDetails.html', context)