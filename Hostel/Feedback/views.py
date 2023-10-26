from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import HostelSerializer, FeedbackSerializer, RoomSerializer
from rest_framework import status

# obtaining all the hostels 
@api_view(['GET', 'POST'])
def hostels(request):
    if request.method == 'GET':
        # Handle the GET request to retrieve all hostels
        hostels = Hostel.objects.all()
        serialized_hostels = HostelSerializer(hostels, many=True)
        return Response(serialized_hostels.data)
    elif request.method == 'POST':
        # Handle the POST request to create a new hostel
        converted = HostelSerializer(data=request.data)
        if converted.is_valid():
            converted.save()
            return Response(converted.data, status=status.HTTP_201_CREATED)
        return Response(converted.errors, status=status.HTTP_400_BAD_REQUEST)


# information about a given hostel
@api_view(['GET', 'PATCH'])
def hostelInfo(request, pk):
    try:
        hostel = Hostel.objects.get(id=pk)
    except Hostel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serialized = HostelSerializer(hostel, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    serialized = HostelSerializer(hostel)
    return Response(serialized.data)



# getting feedback for a given hostel 
@api_view(['GET', 'POST'])
def Feedback(request, pk):
    hostel = Hostel.objects.get(id = pk)
    feeds = hostel.feedback_set.all()
    serialized = FeedbackSerializer(feeds, many = True)
    if request.method == 'POST':
        serialized = FeedbackSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(serialized.data)
    
@api_view(['GET', 'POST'])    
def hostelRooms(request, pk):
    hostel = Hostel.objects.get(id =pk)
    rooms = hostel.room_set.all()
    if request.method == 'POST':
        serialized = RoomSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
    serialized = RoomSerializer(rooms, many= True)
    return Response(serialized.data)


@api_view(['GET', 'PATCH'])
def roomInfo(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    if request.method == 'PATCH':
        serialized = RoomSerializer(room, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    serialized = RoomSerializer(room)
    return Response(serialized.data)   
    

        