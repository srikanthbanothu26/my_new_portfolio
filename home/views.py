from django.shortcuts import render
from .models import PersonalInfo,educationInfo,skillInfo,projectinfo,WebApplicationInfo,WorkexperienceInfo,CertificateInfo


def base(request):
    personal_info=PersonalInfo.objects.all()
    return render(request,"base.html",{"personal_info":personal_info})

def home(request):
    personal_info=PersonalInfo.objects.all()
    return render(request,"index.html",{"personal_info":personal_info})
    
def about(request):
    personal_info=PersonalInfo.objects.all()
    return render(request,"about.html",{"personal_info":personal_info})


def personalinfo(request):
    
    personal_info=PersonalInfo.objects.all()
    return render(request,"personal_info.html",{"personal_info":personal_info})

def educationinfo(request):
    education_info=educationInfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"education.html",{"education_info":education_info,"personal_info":personal_info})

def skillinfo(request):
    skill_info=skillInfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"skills.html",{"skill_info":skill_info,"personal_info":personal_info})

def Projectinfo(request):
    projects=projectinfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"projects.html",{"projects":projects,"personal_info":personal_info})

def certificateinfo(request):
    certificate_info=CertificateInfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"certifications.html",{"certificate_info":certificate_info,"personal_info":personal_info})


def webapplicationsinfo(request):
    webapplications_info=WebApplicationInfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"webapplications.html",{"webapplications_info":webapplications_info,"personal_info":personal_info})


def workexperienceinfo(request):
    workexperience_info=WorkexperienceInfo.objects.all()
    personal_info=PersonalInfo.objects.all()
    return render(request,"workexperience.html",{"workexperience_info":workexperience_info,"personal_info":personal_info})