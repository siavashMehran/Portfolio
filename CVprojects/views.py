from CVprojects.models import Categories, Project
from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.



def projects(request, *args, **kwargs):
    
    projectList = Project.objects.get_all_active()
    categories  = Categories.objects.all()
    mostViewd   = Project.objects.get_most_viewd()[:3]


    #paginator
    paginator = Paginator(projectList, 1, allow_empty_first_page=True)
    pageRequest = request.GET.get('page')
    pageObj = paginator.get_page(pageRequest)

    context = {
        'list'       :  pageObj,
        'categories' :  categories,
        'most_view'  : mostViewd,
        'paginator'  : paginator,
        'pageRequest': pageRequest
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