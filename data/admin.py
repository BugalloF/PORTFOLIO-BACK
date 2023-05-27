from django.contrib import admin
from .models import Skills,ProjectsImages,Projects,Education,JobExperience
from django.contrib.auth.models import Group,User
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title','started_formatted','ended_formatted','language')
    list_filter=('language',)
    # filter_horizontal=('projectImages',)
    def started_formatted(self, obj):
        return obj.started.strftime('%d/%m/%Y')
    
    def ended_formatted(self, obj):
        if obj.ended :
            return obj.ended.strftime('%d/%m/%Y')
        else:
            return obj.ended
    

    started_formatted.short_description = 'Started'
    ended_formatted.short_description = 'Ended'


class SkillsAdmin(admin.ModelAdmin):
    list_display=('title','is_soft_skill','language')
    list_filter=('language','is_soft_skill')

class EducationAdmin(admin.ModelAdmin):
    list_display=('degree','language','started_formatted','ended_formatted')
    list_filter=('language',)
    def started_formatted(self, obj):
        return obj.started.strftime('%d/%m/%Y')
    
    def ended_formatted(self, obj):
        if obj.ended :
            return obj.ended.strftime('%d/%m/%Y')
        else:
            return obj.ended
    started_formatted.short_description = 'Started'
    ended_formatted.short_description = 'Ended'
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(ProjectsImages)
admin.site.register(Education,EducationAdmin)
admin.site.register(JobExperience)
admin.site.register(Skills,SkillsAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = "Fermin Bugallo"
admin.site.site_header = "PORTFOLIO ADMIN"
admin.site.index_title = ""