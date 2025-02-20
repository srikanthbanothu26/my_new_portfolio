from django.urls import path
from .views import home,about,personalinfo,educationinfo,Projectinfo,certificateinfo,webapplicationsinfo,skillinfo,workexperienceinfo

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('personal-info/',personalinfo,name='personal_info'),
    path('education-info/',educationinfo,name='education_info'),
    path('project-info/',Projectinfo,name='project_info'),
    path('certifications/',certificateinfo,name='certifications'),
    path('skills/',skillinfo,name='skills'),
    path('webapplications/',webapplicationsinfo,name='webapplications'),
    path('workexperience/',workexperienceinfo,name='workexperience'),
]
