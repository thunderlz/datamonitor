from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def videolog(request):
    try:
        with open('/mnt/data1/micam/xiaomi_camera_videos/log.txt') as f:
            # return HttpResponse(f.read().replace('\n','<br>'))
            log=f.read().replace('\n','<br>')
            datadic={'log':log}
            render(request,'videomonitor/log.html',context=datadic)
    except:
        return HttpResponse('找不到这个文件。。。')