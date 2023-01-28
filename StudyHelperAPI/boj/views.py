from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Member
from .serializers import Memberserializers
import requests
@api_view(['POST'])
def createMember(request):
    serializer=Memberserializers(data=request.data)
    if serializer.is_valid():
        try:
            member=Member.objects.get(memberId=serializer.validated_data['memberId'])
            return Response("exsists",status=status.HTTP_400_BAD_REQUEST)
        except:
            res = requests.get("https://solved.ac/api/v3/user/problem_stats?handle="+serializer.validated_data["bojId"])
            temp=[]
            for i in range(31):
                temp.append(res.json()[i]["solved"])
            

            serializer.save(bojLev=temp)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
@api_view(['UPDATE'])
def updateMember(request):
    serializer=Memberserializers(data=request.data)
    if serializer.is_valid():
        try:
            member=Member.objects.get(memberId=serializer.validated_data['memberId'])
            res = requests.get("https://solved.ac/api/v3/user/problem_stats?handle="+serializer.validated_data["bojId"])
            temp=[]
            for i in range(31):
                temp.append(res.json()[i]["solved"])
            serializer.save(bojLev=temp)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:    
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
@api_view(['GET'])
def getMember(request):

    try:
        member=Member.objects.get(memberId=request.GET['memberId'])
        serializer=Memberserializers(member)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except:
        return Response("no",status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteMember(request):
    members=Member.objects.all()
    members.delete()
    return Response("deleted",status=status.HTTP_200_OK)
@api_view(['GET'])
def getAll(request):
        member=Member.objects.all()
        serializer=Memberserializers(member,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
