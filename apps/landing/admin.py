from django.contrib import admin
from landing.models import StaticPage,Media,Porto

class StaticPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(StaticPage,StaticPageAdmin)
admin.site.register(Media)
admin.site.register(Porto)