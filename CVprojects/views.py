
from CVprojects.models import Categories, Project
from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.

def ss(s):
    print()
    print()
    print(s)
    print()
    print()

def projects(request, *args, **kwargs):

    #QuerrySet
    projectList = Project.objects.get_all_active()

    #paginator
    paginator = Paginator(projectList, 1, allow_empty_first_page=True)
    pageRequest = request.GET.get('page')
    pageObj = paginator.get_page(pageRequest)

    context = {
        'list'       :  pageObj,
        'paginator'  : paginator,
        'pageRequest': pageRequest
    }
    return render(request, 'projects.html', context)


def search(request, cat:str, *args, **kwargs):
    #QuerrySet
    cat = cat.replace("_", " ")
    category = Categories.objects.get_related_projects_or_none(cat)
    
    # paginator
    
    paginator = Paginator(category, 1, allow_empty_first_page=True)
    pageRequest = request.GET.get('page')
    pageObj = paginator.get_page(pageRequest)

    # Validation

    context = {
        'list'       :  pageObj,
        'paginator'  : paginator,
        'pageRequest': pageRequest
    }
    return render(request, 'search.html', context)


def projectDetailView(request, slug):

    project = Project.objects.getProjectbySlug(slug)
    project.viewsPlusOne()
    allTechs = project.get_project_techs()
        

    
    context = {
        'project'   : project,
        'techs' : allTechs
    }

    return render(request, 'projectDetails.html', context)