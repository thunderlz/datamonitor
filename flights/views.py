from django.shortcuts import render
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
engine=create_engine('mysql+pymysql://root:751982leizhen@192.168.31.199/saflights')

# Create your views here.

def todayflights(request):
    if request.method=='GET':
        queryday=datetime.now().strftime('%Y%m%d')
        depport=''
        arrport=''
        depdate=''
    else:
        queryday=request.POST.get('querydate')
        depport=request.POST.get('depport')
        arrport=request.POST.get('arrport')
        depdate=request.POST.get('depdate')
    sql='''select airLine  ,arrDate ,arrPort ,arrTime ,arrivalTerminal ,codeShare ,codeShareInfo ,
    depDate ,depPort ,depTime ,departureTerminal ,flightNo ,meal ,plane ,rate 
    ,timeDuringFlight ,lowprice ,querydate from flights 
    where querydate like "{}%%" and depport like "%%{}%%" and arrport like "%%{}%%" and depdate like "%%{}%%" '''.format(queryday,depport,arrport,depdate)

    df=pd.read_sql(sql,con=engine)
    flights={"flights":df.iterrows(),'flights_columns':df.columns,'flights_count':df.shape[0],'queryparam':{'queryday':queryday,'depport':depport,'arrport':arrport,'depdate':depdate}}
    datadic={'flights':flights}
    return render(request,'flights/todayflights.html',context=datadic)