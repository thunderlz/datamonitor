from django.shortcuts import render
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
engine=create_engine('mysql+pymysql://root:751982leizhen@192.168.31.199/saflights')

# Create your views here.

def todayflights(request):
    today=datetime.now().strftime('%Y%m%d')
    sql='''select airLine  ,arrDate ,arrPort ,arrTime ,arrivalTerminal ,codeShare ,codeShareInfo ,
    depDate ,depPort ,depTime ,departureTerminal ,flightNo ,meal ,plane ,rate 
    ,timeDuringFlight ,lowprice ,querydate from flights where querydate like "{}%%"'''.format(today)
    # sql='''select airLine  ,arrDate ,arrPort ,arrTime ,arrivalTerminal ,codeShare ,codeShareInfo ,
    # depDate ,depPort ,depTime ,departureTerminal ,flightNo ,meal ,plane ,rate ,roundTripCabin 
    # ,segInterval ,stopNameEn ,stopNameZh  ,stopNumber ,term ,timeDuringFlight ,timeDuringFlightEn  
    # ,lowprice ,querydate from flights limit 200'''
    df=pd.read_sql(sql,con=engine)
    flights={"flights":df.iterrows(),'flights_columns':df.columns,'flights_count':df.shape[0]}
    datadic={'flights':flights}
    return render(request,'flights/todayflights.html',context=datadic)