from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def videolog(request):
    try:
        with open('/mnt/data1/micam/xiaomi_camera_videos/log.txt') as f:
            return HttpResponse(f.read().replace('\n','<br>'))
    except:
        return HttpResponse('找不到这个文件。。。')