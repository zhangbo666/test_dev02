from django.contrib import admin

# Register your models here.


from module_app.models import Module


class ModuleAdmin(admin.ModelAdmin):

        list_display = ['name','describe','create_time']

        search_fields = ['name']


admin.site.register(Module,ModuleAdmin)