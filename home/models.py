from django.db import models

class PersonalInfo(models.Model):
    
    first_name = models.CharField("First Name", max_length=200, null=True, blank=True)
    middle_name = models.CharField("Middle Name", max_length=200, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=200, null=True, blank=True)
    date_of_birth=models.DateField("DOB",null=True, blank=True)
    mobile_number=models.CharField("Mobile Number",max_length=12,blank=True)
    email_id=models.CharField("Email",max_length=255,blank=True)
    linked_in=models.CharField("Linked-in",blank=True)
    github=models.CharField("Github",blank=True)
    twitter=models.CharField("Twitter",blank=True)
    embedded_location=models.CharField("Embedded Location",blank=True)
    objective=models.TextField("Describe Yourself",blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    
class ProfileImages(models.Model):
    
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name="user",default=None)  # Add related_name
    image=models.ImageField("image")

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

class Category(models.Model):
    
    project = models.ForeignKey('projectinfo', on_delete=models.CASCADE, related_name="proj_category",default=None)  # Add related_name
    name = models.CharField("Category", max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Technology(models.Model):
    
    project = models.ForeignKey('projectinfo', on_delete=models.CASCADE, related_name="proj_technology",default=None)  # Add related_name
    name = models.CharField("Technology", max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    project = models.ForeignKey('projectinfo', on_delete=models.CASCADE, related_name="project_feature",null=True, blank=True)  
    name = models.CharField("Feature Name", max_length=255)
    description = models.TextField("Description", null=True, blank=True)

    def __str__(self):
        return self.name


class ProcessStep(models.Model):
    
    project = models.ForeignKey('projectinfo', on_delete=models.CASCADE, related_name='project_step',default=None)
    step_number = models.PositiveIntegerField("Step Number")
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Step Description")

    class Meta:
        ordering = ['step_number']  # Ensures steps are ordered correctly

    def __str__(self):
        return f"Step {self.step_number}: {self.description[:50]}"
    
class projectinfo(models.Model):
    
    name = models.TextField("Name", null=True, blank=True)
    overview = models.TextField("Overview", null=True, blank=True)
    start_date = models.DateField("Start Date", null=True, blank=True)
    end_date = models.DateField("End Date", null=True, blank=True)
    repository_link = models.URLField("Repository Link", max_length=255, null=True, blank=True)
    status = models.CharField(
        "Status",
        max_length=50,
        choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')],
        default='Completed'
    )

    def __str__(self):
        return f"{self.name} ,{self.status}"

class CertificateInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class CertificateAttachment(models.Model):
    certificate = models.ForeignKey(CertificateInfo, related_name="attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to="certificates/")

    def __str__(self):
        return f"{self.certificate.name} - {self.file.name}"
    
class WorkexperienceInfo(models.Model):
    
    name = models.CharField("Name", null=True, blank=True)
    company=models.CharField("Company",null=True, blank=True)
    join_date = models.DateField("Start Date",null=True, blank=True)
    end_date=models.DateField("End Date", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.join_date} {self.end_date}"
    
    
class Workkeyresponsiblities(models.Model):
    key_responsiblity = models.ForeignKey(WorkexperienceInfo, related_name="key_responsiblity", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=1000,null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class WebApplicationInfo(models.Model):
    
    name = models.CharField("Name", max_length=255, default=None)
    description = models.TextField("Description", default=None)
    technologies = models.TextField("Technologies Used", default=None)
    github_url = models.URLField("GitHub Repository", default=None)

    def __str__(self):
        return f"{self.name} - {self.technologies}"

         