from django.db import models
from datetime import datetime
from datetime import timezone


# Create your models here.

class Cam_video(models.Model):

    cam=models.CharField("摄像头", max_length=50)
    cam_hour=models.CharField("小时文件夹", max_length=50)
    cam_filename=models.CharField("文件名", max_length=50)
    cc_datetime=models.ForeignKey("Cam_check", verbose_name='检查时间', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "摄像机视频"
        verbose_name_plural = "摄像机视频"

    def __str__(self):
        return self.cam_filename

    def get_absolute_url(self):
        return reverse("Cam_video_detail", kwargs={"pk": self.pk})

class Cam_check(models.Model):

    cc_datetime=models.DateTimeField("检查时间", auto_now=False, auto_now_add=True)
    cc_camcount=models.IntegerField('摄像头数量')
    cc_hourcount=models.IntegerField('文件夹数量')
    cc_videocount=models.IntegerField('视频文件数量')
    cc_comment=models.TextField('备注')

    class Meta:
        verbose_name = "视频检查"
        verbose_name_plural = "视频检查"

    def __str__(self):
        return self.cc_datetime.strftime('%Y年%m月%d日%H时%M分')

    def get_absolute_url(self):
        return reverse("Cam_check_detail", kwargs={"pk": self.pk})

