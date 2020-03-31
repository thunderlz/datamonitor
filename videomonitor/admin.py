from django.contrib import admin
from videomonitor.models import Cam_video,Cam_check

# Register your models here.

class videoInline(admin.TabularInline):
# class videoInline(admin.StackedInline):
    model = Cam_video
    extra=0
    list_per_page=10

@admin.register(Cam_video)
class Cam_videoAdmin(admin.ModelAdmin):
    list_display=['id','cam','cam_hour','cam_filename','cc_datetime']
    list_filter=['cam','cc_datetime']
    list_per_page = 50

@admin.register(Cam_check)
class Cam_checkAdmin(admin.ModelAdmin):
    list_display=['id','cc_datetime','cc_camcount','cc_videocount','cc_comment']
    list_per_page = 50
    # inlines=[videoInline]

# admin.site.register(Cam_video,Cam_videoAdmin)
