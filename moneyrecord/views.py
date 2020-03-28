from django.shortcuts import render
from django.http import HttpResponse
from moneyrecord.models import Allmoney,Detailmoney

# Create your views here.


def moneyrecord(requests):
    # return HttpResponse('moneyrecord')
    allmoneys=Allmoney.objects.filter(degree__lte=3)
    # print(dir(allmoneys[4]))
    detailmoneys=Detailmoney.objects.all()
    print(detailmoneys[0].allmoney.money)
    datadic={'allmoneys':allmoneys,'detailmoneys':detailmoneys}
    return render(requests,'moneyrecord/show.html',context=datadic)