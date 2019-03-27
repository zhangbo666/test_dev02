from django.contrib import admin

# Register your models here.


from personal.models.project import Project
from personal.models.module import Module


class ProjectAdmin(admin.ModelAdmin):

        list_display = ['name','describe','status','create_time','update_time']


class ModuleAdmin(admin.ModelAdmin):

        list_display = ['name','describe','create_time']



admin.site.register(Project,ProjectAdmin)

admin.site.register(Module,ModuleAdmin)