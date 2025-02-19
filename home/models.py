from django.db import models

class PersonalInfo(models.Model):
    
    first_name = models.CharField("First Name", max_length=200, null=True, blank=True)
    middle_name = models.CharField("Middle Name", max_length=200, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=200, null=True, blank=True)
    mobile_number=models.CharField("Mobile Number",max_length=12,blank=True)
    email_id=models.CharField("Email",max_length=255,blank=True)
    linked_in=models.CharField("Linked-in",blank=True)
    github=models.CharField("Github",blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class educationInfo(models.Model):
    
    name = models.CharField("Education Name", null=True, blank=True)
    institute = models.CharField("school or College Name", null=True, blank=True)
    specilization = models.CharField("specilization", null=True, blank=True)
    join_date = models.DateField("Start Date",null=True, blank=True)
    end_date=models.DateField("End Date", null=True, blank=True)
    marks=models.CharField("Marks or Perecentage or GPA", blank=True)

    def __str__(self):
        return f"{self.name} {self.institute} {self.specilization}"
    
    

class skillInfo(models.Model):
    
    name = models.CharField("Skill", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"


class ProjectInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.description}"
    

class CertificateInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.description}"
    
class WorkexperienceInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    join_date = models.DateField("Start Date",null=True, blank=True)
    end_date=models.DateField("End Date", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.description} {self.join_date} {self.end_date}"
    
class WebApplicationInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    technologies= models.TextField("Technologies Used", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.description} {self.technologies}"