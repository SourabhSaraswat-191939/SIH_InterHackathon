import re
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from firstRevise.models import Registration
from firstRevise.serialization import Serializationclass, Serializationsort
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
        # print("this is post",request.data['collegeName'])
        #TLR=(studentStrength*20)/10000+facultyStudentRatio*25+(facultyExperience*20)/50+(financialResource*20)/10000000+(onlineEducation*15)/500
        #publication=(combPublicationMetric*35)/100+(qualOfPublication*35)/100+(iprPatents*15)/100+(footPrint*15)/100
        #outcome=(graduationOutcome*60)/10000+(phdOutcome*40)/1000
        #outreach=(otherStatesStudent*30)/5000+(womenPercentage*30)/8000+(economicallyChallenged*20)/2000+(physicallyChallenged*20)/500
        #perceptionS=perception*100
        #total=TLR*0.30+publication*0.30+outcome*0.20+outreach*0.10+perceptionS*0.10
        TLR=(request.data['studentStrength']*20)/10000+request.data['facultyStudentRatio']*25+(request.data['facultyExperience']*20)/50+(request.data['financialResource']*20)/10000000+(request.data['onlineEducation']*15)/500
        publication=(request.data['combPublicationMetric']*35)/100+(request.data['qualOfPublication']*35)/100+(request.data['iprPatents']*15)/100+(request.data['footPrint']*15)/100
        outcome=(request.data['graduationOutcome']*60)/10000+(request.data['phdOutcome']*40)/1000
        outreach=(request.data['otherStateStudent']*30)/5000+(request.data['womenPercentage']*30)/8000+(request.data['economicallyChallenged']*20)/2000+(request.data['physicallyChallenged']*20)/500
        perceptionS=request.data['perception']*100
        total=TLR*0.30+publication*0.30+outcome*0.20+outreach*0.10+perceptionS*0.10-2

        instance = Registration(total=total,collegeName=request.data['collegeName'],city=request.data['city'],state=request.data['state'],pinCode=request.data['pinCode'],studentStrength=request.data['studentStrength'],facultyStudentRatio=request.data['facultyStudentRatio'],facultyExperience=request.data['facultyExperience'],financialResource=request.data['financialResource'],onlineEducation=request.data['onlineEducation'],combPublicationMetric=request.data['combPublicationMetric'],qualOfPublication=request.data['qualOfPublication'],iprPatents=request.data['iprPatents'],footPrint=request.data['footPrint'],graduationOutcome=request.data['graduationOutcome'],phdOutcome=request.data['phdOutcome'],otherStateStudent=request.data['otherStateStudent'],womenPercentage=request.data['womenPercentage'],economicallyChallenged=request.data['economicallyChallenged'],physicallyChallenged=request.data['physicallyChallenged'],perception=request.data['perception'])
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
        results = Registration.objects.order_by('total').reverse()
        serialize = Serializationsort(results,many=True)
        print("Get Request occured.")
        return Response(serialize.data)