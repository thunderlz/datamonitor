from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from videomonitor.models import Cam_video, Cam_check
import glob
import pandas as pd
import socket

if socket.gethostname()=='lznbserver':
    cam_path='/mnt/data1/micam/xiaomi_camera_videos/'
else:
    cam_path = '/Volumes/micamsdir/xiaomi_camera_videos/'



def getvideofiles(cam_path):
    ret = []
    micams = glob.glob(cam_path+'/5ce50*')
    for micam in micams:
        hours = glob.glob(micam+'/202*')
        for hour in hours:
            videos = glob.glob(hour+'/*.mp4')
            for video in videos:
                ret.append([micam.split('/')[-1], hour.split('/')[-1],
                            video.split('/')[-1]])
    return ret


# Create your views here.


def videolog(request):
    try:
        log_path = cam_path+'log.txt'
        with open(log_path, 'rt') as f:
            log = f.read().replace('\n', '<br>')
            datadic = {'log': log}
            return render(request, 'videomonitor/log.html', context=datadic)
    except:
        return HttpResponse('找不到这个文件。。。')


def video(request):
    global cam_videos
    global selected_cc_datetime_id
    if request.GET.get('cam'):
        selected_cc_datetime_id = request.GET.get('cam')
        cam_videos = Cam_video.objects.filter(
            cc_datetime_id=request.GET.get('cam'))
    elif (not request.GET.get('cam')) and (not request.GET.get('page')):
        cam_videos = Cam_video.objects.all()
        selected_cc_datetime_id = 0
    cam_video_pages = Paginator(cam_videos, 100)
    page_obj = cam_video_pages.get_page(request.GET.get('page'))
    datadic = {'page_obj': page_obj, 'cam_checks': Cam_check.objects.all(),'selected_cc_datetime_id':int(selected_cc_datetime_id)}

    return render(request, 'videomonitor/videomonitor.html', context=datadic)


def videocheck(request):
    # 视频监控文件确认，如果出现没有传的情况就体现出来。
    cam_videos = []
    ret = getvideofiles(cam_path)

    df = pd.DataFrame(ret, columns=['cam', 'hour', 'filename'])
    cam_check = Cam_check()
    cam_check.cc_camcount = df['cam'].unique().shape[0]
    cam_check.cc_hourcount = df['hour'].unique().shape[0]
    cam_check.cc_videocount = df.shape[0]
    cam_check.save()

    for item in ret:
        cam_videos.append(Cam_video(
            cam=item[0], cam_hour=item[1], cam_filename=item[2], cc_datetime_id=cam_check.id))

    Cam_video.objects.bulk_create(cam_videos)
    # return JsonResponse(ret,safe=False)
    return redirect(reverse('video'))
