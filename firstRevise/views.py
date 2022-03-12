import re
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from firstRevise.models import Registration
from firstRevise.serialization import Serializationclass
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from firstRevise.serialization import Serializationclass

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def register(request):
    if request.method=='POST':
        print("this is post",request.data['collegeName'])
        instance = Registration(collegeName=request.data['collegeName'],city=request.data['city'],state=request.data['state'],pinCode=request.data['pinCode'],totalPhdStudents=request.data['totalPhdStudents'],totalStudentsApproved=request.data['totalStudentsApproved'],totalStudents=request.data['totalStudents'],numOfFaculties=request.data['numOfFaculties'],facultyExpLT8=request.data['facultyExpLT8'],facultyExp8To15=request.data['facultyExp8To15'],facultyExpGT15=request.data['facultyExpGT15'],avgAnnualCapPerStd=request.data['avgAnnualCapPerStd'],operExp=request.data['operExp'],numOfPublication=request.data['numOfPublication'],numOfCitation=request.data['numOfCitation'],totalPatentPublished=request.data['totalPatentPublished'],totalPatentGranted=request.data['totalPatentGranted'],totalResearchFunding=request.data['totalResearchFunding'],annualConsultancyAmount=request.data['annualConsultancyAmount'],totalExecutiveEarning=request.data['totalExecutiveEarning'],totalStudentPassed=request.data['totalStudentPassed'],totalPhdStudentPassed=request.data['totalPhdStudentPassed'],studentFromOtherStates=request.data['studentFromOtherStates'],percOfWomenFaculty=request.data['percOfWomenFaculty'],womenStudentNumbers=request.data['womenStudentNumbers'],physChallengedStd=request.data['physChallengedStd'],eAndSociallyChallengedStd=request.data['eAndSociallyChallengedStd'])
        instance.save()
        return Response({"message": "Post message requested."},status=200)
    return Response({"message": "Get message requested."})
    # else:
    #     data = Registration.objects.all()
    #     # serializers.serialize('json', self.get_queryset())
    #     return JsonResponse({"message": "Hello Rachit, world!"})
    # return Response({"message": "Hello Rachit, world!","data":data})

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def publish(request):
    if request.method=='GET':
        results = Registration.objects.all()
        serialize = Serializationclass(results,many=True)
        print("Get Request occured.")
        return Response(serialize.data)