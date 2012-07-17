from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)
    permalink = models.SlugField()
    publish = models.BooleanField()
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    class Meta :
        verbose_name_plural = "Daftar Halaman"
        
    def __unicode__(self):
        return self.title
