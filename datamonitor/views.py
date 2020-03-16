from django.shortcuts import render
from datetime import datetime

def index(request):
    datadic={'title':'首页','now':datetime.now().strftime('%y年%m月%d日%H时%M分%S秒')}
    return render(request,'index.html',context=datadic)