import os,config
from django.conf import settings
from django.db import models
from django.template import Template 
from livesettings import config_value



class StaticPage(models.Model):
    
    def get_base_template():
        tmp_dir = settings.TEMPLATE_DIRS[0]
        theme = config_value('landing','THEME')
        theme_dir = os.path.join(tmp_dir,theme)
        list_dir = os.listdir(os.path.join(theme_dir,'skeletons/base'))
        return [ (x,x) for x in list_dir ]
    
    def node_to_dict(self):
        hasil = {}
        raw_tmp = Template(self.content)
        for data in raw_tmp.nodelist :
            if data.__dict__.get('name'):
                hasil[data.__dict__.get('name')] = data.nodelist[0].s
        return hasil

        
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.title
       

    
class Media(models.Model):
    name = models.CharField(max_length=255)
    files = models.FileField(upload_to='public')
    
    def __unicode__(self):
        return self.name 

class Porto(models.Model):
    title = models.CharField(max_length=255)
    main_picture = models.ImageField(upload_to='porto/main_picture')
    description = models.TextField()
    website = models.URLField(max_length=255,null=True,blank=True)
    other_media = models.ManyToManyField(Media,blank=True,null=True)
    
    def __unicode__(self):
        return self.title