from statistics import mode
from django.db import models

# Create your models here.
class Registration(models.Model):
    collegeName= models.CharField(max_length=100)
    city= models.CharField(max_length=40)
    state= models.CharField(max_length=40)
    pinCode= models.IntegerField()
    # email= models.EmailField()
    total = models.FloatField()
    # TLR
    studentStrength = models.FloatField()
    facultyStudentRatio = models.FloatField()
    facultyExperience = models.FloatField()
    financialResource = models.FloatField()
    onlineEducation = models.FloatField()

    # R&PP
    combPublicationMetric = models.FloatField()
    qualOfPublication = models.FloatField()
    iprPatents = models.FloatField()
    footPrint = models.FloatField()

    # GO
    graduationOutcome = models.FloatField()
    phdOutcome = models.FloatField()
    
    # O&I
    otherStateStudent = models.FloatField()
    womenPercentage = models.FloatField()
    economicallyChallenged = models.FloatField()
    physicallyChallenged = models.FloatField()
    perception = models.FloatField()


    # collegeName= models.CharField(max_length=100)
    # city= models.CharField(max_length=40)
    # state= models.CharField(max_length=40)
    # pinCode= models.IntegerField()
    # # email= models.EmailField()
    
    # # TLR
    # totalPhdStudents = models.IntegerField()
    # totalStudentsApproved = models.IntegerField()
    # totalStudents = models.IntegerField()
    # numOfFaculties = models.IntegerField()
    # facultyExpLT8 = models.IntegerField()
    # facultyExp8To15 = models.IntegerField()
    # facultyExpGT15 = models.IntegerField()
    # avgAnnualCapPerStd = models.FloatField()
    # operExp = models.IntegerField()

    # # R&PP
    # numOfPublication = models.IntegerField()
    # numOfCitation = models.IntegerField()
    # totalPatentPublished = models.IntegerField()
    # totalPatentGranted = models.IntegerField()
    # totalResearchFunding = models.IntegerField()
    # annualConsultancyAmount = models.IntegerField()
    # totalExecutiveEarning = models.IntegerField()


    # # GOOI
    # totalStudentPassed = models.IntegerField()
    # totalPhdStudentPassed = models.IntegerField()
    # studentFromOtherStates = models.IntegerField()
    # percOfWomenFaculty = models.FloatField()
    # womenStudentNumbers = models.IntegerField()
    # physChallengedStd = models.IntegerField()
    # eAndSociallyChallengedStd = models.IntegerField()   # econimically and socially chalenged students


    # # active: models.BooleanField(default=False)