from django.contrib import admin
from .models import Skills,ProjectsImages,Projects,Education,JobExperience
from django.contrib.auth.models import Group,User
# Register your models here.
admin.site.register(Skills)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('started_formatted','ended_formatted')

    def started_formatted(self, obj):
        return obj.started.strftime('%d/%m/%Y')
    
    def ended_formatted(self, obj):
        if obj.ended :
            return obj.ended.strftime('%d/%m/%Y')
        else:
            return obj.ended

    started_formatted.short_description = 'Started'
    ended_formatted.short_description = 'Started'
admin.site.register(Projects)
admin.site.register(ProjectsImages)
admin.site.register(Education)
admin.site.register(JobExperience)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = "Fermin Bugallo"
admin.site.site_header = "PORTFOLIO ADMIN"
admin.site.index_title = ""