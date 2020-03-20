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
        depdate=datetime.now().strftime('%Y%m%d')
    else:
        queryday=request.POST.get('querydate')
        depport=request.POST.get('depport')
        arrport=request.POST.get('arrport')
        depdate=request.POST.get('depdate')
    sql='''select airLine 航空公司,arrDate 降落日期,arrPort 降落机场,arrTime 降落时间,arrivalTerminal 到达航站楼,codeShare 是否共享,codeShareInfo 共享航班号,
    depDate 起飞日期,depPort 起飞机场,depTime 起飞时间,departureTerminal 起飞航站楼,flightNo 航班号,meal 是否餐食,plane 飞机型号,rate 准点率
    ,timeDuringFlight 飞行时间,lowprice 最低价,querydate 查询日期 from flights 
    where querydate like "{}%%" and depport like "%%{}%%" and arrport like "%%{}%%" and depdate like "%%{}%%" '''.format(queryday,depport,arrport,depdate)

    df=pd.read_sql(sql,con=engine)
    flights={"flights":df.iterrows(),'flights_columns':df.columns,'flights_count':df.shape[0],'queryparam':{'queryday':queryday,'depport':depport,'arrport':arrport,'depdate':depdate}}
    datadic={'flights':flights}
    return render(request,'flights/todayflights.html',context=datadic)