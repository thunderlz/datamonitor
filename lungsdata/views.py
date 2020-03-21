from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from sqlalchemy import create_engine
import pandas as pd
engine=create_engine('mysql+pymysql://root:751982leizhen@192.168.31.200/lungsdata')
# Create your views here.

def lungsdata(request):
    sql='select * from jsondata order by time desc limit 1'
    df=pd.read_sql(sql,con=engine)
    return HttpResponse(df.iat[0,1]+df.iat[0,0])