from django.shortcuts import render
from .models import PersonalInfo,educationInfo,skillInfo,projectinfo,WebApplicationInfo,WorkexperienceInfo,CertificateInfo


def home(request):
    return render(request,"index.html")
    
def about(request):
    
    return render(request,"about.html")


def personalinfo(request):
    
    personal_info=PersonalInfo.objects.all()
    return render(request,"personal_info.html",{"personal_info":personal_info})

def educationinfo(request):
    education_info=educationInfo.objects.all()
    return render(request,"education.html",{"education_info":education_info})

def skillinfo(request):
    skill_info=skillInfo.objects.all()
    return render(request,"skills.html",{"skill_info":skill_info})

def Projectinfo(request):
    projects=projectinfo.objects.all()
    return render(request,"projects.html",{"projects":projects})

def certificateinfo(request):
    certificate_info=CertificateInfo.objects.all()
    return render(request,"certifications.html",{"certificate_info":certificate_info})


def webapplicationsinfo(request):
    webapplications_info=WebApplicationInfo.objects.all()
    return render(request,"webapplications.html",{"webapplications_info":webapplications_info})


def workexperienceinfo(request):
    workexperience_info=WorkexperienceInfo.objects.all()
    return render(request,"workexperience.html",{"workexperience_info":workexperience_info})