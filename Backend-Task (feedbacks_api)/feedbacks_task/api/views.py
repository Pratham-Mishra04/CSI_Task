import json
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from  .models import Feedback
from .serializers import FeedbackSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Instructions':'Please add the following to your url to do the corresponding operation',
        'List':'feed-detail/',
        'Detail View':'/feed-detail/(feed_id)/',
        'Create':'/feed-create',
        'Update':'/feed-update/(feed_id)/',
        'Delete':'/feed-delete/(feed_id)/',
        'Please Note':"The Create and Update method items should be entered in form of {'name'='your name','feed'='your feedback'}"

    }
    return Response(api_urls)

@api_view(['GET'])
def feedList(request):
    feeds=Feedback.objects.all()
    serializer=FeedbackSerializer(feeds, many=True)
    return Response(serializer.data)


def landing(request):
    return HttpResponse("<strong>This is the landing page for feedback api. Please go to /api to access the data</strong>")

@api_view(['GET'])
def feedDetail(request,pk):
    feeds=Feedback.objects.get(id=pk)
    serializer=FeedbackSerializer(feeds, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def feedCreate(request):
    serializer=FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Feedback Successfully Added")
    else:
        return Response("Please Input Valid Data")

@api_view(['POST'])
def feedUpdate(request,pk):
    feed=Feedback.objects.get(id=pk)
    serializer=FeedbackSerializer(instance=feed, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Feedback Successfully Added")
    else:
        return Response("Please Input Valid Data")

@api_view(['DELETE'])
def feedDelete(request,pk):
    feed=Feedback.objects.get(id=pk)
    feed.delete()
    return Response("Feedback Deleted!")
