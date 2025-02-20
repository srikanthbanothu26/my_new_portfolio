from django.contrib import admin
from .models import PersonalInfo,educationInfo,skillInfo,projectinfo,CertificateInfo,WebApplicationInfo,WorkexperienceInfo,Feature,ProcessStep,Category,Technology,CertificateAttachment,Workkeyresponsiblities,ProfileImages


class TabularlineprofileImage(admin.TabularInline):
    model = ProfileImages
    extra = 1
    
class Tabularlinefeature(admin.TabularInline):
    model = Feature
    extra = 1

class TabularlineProcessStep(admin.TabularInline):
    model = ProcessStep
    extra = 1
    
class TabularlineCategory(admin.TabularInline):
    model = Category
    extra = 1
    
class TabularlineTechnology(admin.TabularInline):
    model = Technology
    extra = 1

class TabularlineCertificate(admin.TabularInline):
    model = CertificateAttachment
    extra = 1
    
class Tablularkeyresponsiblities(admin.TabularInline):
    model = Workkeyresponsiblities
    extra = 1
    
class educationInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "institute", "specilization","join_date","end_date","marks")

class skillInfoAdmin(admin.ModelAdmin):
    list_display = ["name"]
    # inlines = [TabularInlinePersonalInfo] 
class PersonalInfoAdmin(admin.ModelAdmin):
    inlines=[TabularlineprofileImage]
    
class ProjectsAdmin(admin.ModelAdmin):
    inlines=[TabularlineProcessStep, TabularlineTechnology, Tabularlinefeature, TabularlineCategory]
    
class CertificateInfoAdmin(admin.ModelAdmin):
    inlines=[TabularlineCertificate]
    
class WebApplicationInfoAdmin(admin.ModelAdmin):
    list_display=["name"]
   
class WorkexperienceInfoAdmin(admin.ModelAdmin):
    inlines=[Tablularkeyresponsiblities]
    
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(educationInfo,educationInfoAdmin)
admin.site.register(skillInfo,skillInfoAdmin)
admin.site.register(projectinfo,ProjectsAdmin)
admin.site.register(CertificateInfo,CertificateInfoAdmin)
admin.site.register(WorkexperienceInfo,WorkexperienceInfoAdmin)
admin.site.register(WebApplicationInfo,WebApplicationInfoAdmin)
