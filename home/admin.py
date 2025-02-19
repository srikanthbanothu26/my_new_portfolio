from django.contrib import admin
from .models import PersonalInfo,educationInfo,skillInfo,ProjectInfo,CertificateInfo,WebApplicationInfo,WorkexperienceInfo

# class TabularInlinePersonalInfo(admin.TabularInline):
#     model = PersonalInfo
#     extra = 1
class educationInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "institute", "specilization","join_date","end_date","marks")

class skillInfoAdmin(admin.ModelAdmin):
    list_display = ["name"]
    # inlines = [TabularInlinePersonalInfo] 
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name","mobile_number","email_id","linked_in","github")
    
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    
class CertificateInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    
class WebApplicationInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "technologies")
   
class WorkexperienceInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "join_date","end_date")
    
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(educationInfo,educationInfoAdmin)
admin.site.register(skillInfo,skillInfoAdmin)
admin.site.register(ProjectInfo,ProjectInfoAdmin)
admin.site.register(CertificateInfo,CertificateInfoAdmin)
admin.site.register(WorkexperienceInfo,WorkexperienceInfoAdmin)
admin.site.register(WebApplicationInfo,WebApplicationInfoAdmin)
