from django.shortcuts import render_to_response
from livesettings import config_value

def home(request):
    theme = config_value('landing','THEME')
    return render_to_response(theme+'/skeletons/base.html')
