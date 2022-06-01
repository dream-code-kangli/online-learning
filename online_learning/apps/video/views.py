from django.http import JsonResponse
from django.shortcuts import render
from .serializers import VideoSerializers
from .models import Video
from rest_framework import generics

# Create your views here.
class VideoAPI(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

class VideoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

def addViews(request):
    pk = request.GET.get('pk')
    v = Video.objects.filter(pk=pk).first()
    v.views = int(v.views) + 1
    v.save()
    return JsonResponse({
        'status': 200
    })

def addPraise(request):
    pk = request.GET.get('pk')
    v = Video.objects.filter(pk=pk).first()
    v.praise_num = int(v.praise_num) + 1
    v.save()
    return JsonResponse({
        'status': 200,
        'msg': '点赞成功'
    })
