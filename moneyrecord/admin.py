from django.contrib import admin
from moneyrecord.models import Allmoney
from moneyrecord.models import Detailmoney


# Register your models here.

# 这种方式是最简单的，不用新增一个modelAdmin的类
# admin.site.register(Allmoney)

@admin.register(Allmoney)
class AllmoneyAdmin(admin.ModelAdmin):
    list_display = ('time', 'money')
    search_fields = ('time', 'money')
    list_filter = ('time', 'money',)


@admin.register(Detailmoney)
class DetailmoneyAdmin(admin.ModelAdmin):
    list_display = ('allmoney', 'jingdong', 'zhifubao', 'huabei', 'baitiao',)
    # search_fields = ('allmoney', 'jingdong', 'zhifubao', 'huabei', 'baitiao')
    list_filter = ('allmoney',)
