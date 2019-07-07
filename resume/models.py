from django.db import models
import django.db.models
from django.contrib.auth.models import User
import uuid

class UserLogin(models.Model):
    FirstNameLogin = models.CharField(max_length=25)
    # DateOfBirthLogin = models.DateField()
    def __str__(self):
        return self.FirstNameLogin

# Create your models here.
class ResDetails(models.Model):
     # user = models.ForeignKey(User)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    MobileNumber = models.CharField(max_length=10)
    ResidentailAddress = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    Pincode = models.CharField(max_length=7)
    DateOfBirth = models.DateField()
    Summary = models.CharField(max_length=100)
    EducationSummary = models.CharField(max_length=100)
    CollegeName = models.CharField(max_length=25)
    Cgpa = models.CharField(max_length=25)
    JobTitle = models.CharField(max_length=25)
    Company = models.CharField(max_length=25)
    Location = models.CharField(max_length=25)
    WorkSummary = models.CharField(max_length=100)
    HobbiesSummary = models.CharField(max_length=100)
    Skill = models.CharField(max_length=25)
    SkillSummary = models.CharField(max_length=100)
    Language = models.CharField(max_length=25)
    RefName = models.CharField(max_length=25)
    RefNo = models.CharField(max_length=25)
    RefAdd = models.CharField(max_length=25)
    RefEmail = models.EmailField(max_length=25)
    RefCompany = models.CharField(max_length=25)
    

    def __str__(self):
        return self.FirstName
    
    def splitsummary(self):
        return self.Summary.split('.')
    
    def spliteducationsummary(self):
        return self.EducationSummary.split('.')
    
    def splitworksummary(self):
        return self.WorkSummary.split('.')
    
    def splithobbiessummary(self):
        return self.HobbiesSummary.split('.')

    def splitskillsummary(self):
        return self.SkillSummary.split('.')

    def splitlang(self):
        return self.Language.split('.')