from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from livesettings import config_value
from landing.models import StaticPage,Porto
import config

def home(request):
    theme = config_value('landing','THEME')
    return render_to_response(theme+'/skeletons/home.html')
    
def static_page(request,slug):
    if slug == 'beranda' :
        return redirect('/')
        
    theme = config_value('landing','THEME')
    try :
        static_page = StaticPage.objects.get(slug=slug)
    except :
        return render_to_response(theme+'/skeletons/404.html')
    return render_to_response(theme+'/skeletons/static.html',{
        'static_page' : static_page
    },context_instance=RequestContext(request))
    
def porto_list(request):
    theme = config_value('landing','THEME')
    porto = Porto.objects.all()
    paginator = Paginator(porto, 1) 
    page = request.GET.get('page')
    try:
        portos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        portos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        portos = paginator.page(paginator.num_pages)
    return render_to_response(theme+'/skeletons/porto.html',{
        'porto_list' : portos
    },context_instance=RequestContext(request))