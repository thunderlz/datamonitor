from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd


engine=create_engine('mysql+pymysql://root:751982leizhen@192.168.31.200:3306/leizquant')

# Create your views here.

def stocklastday(request):
    # return HttpResponse('收到请求！')

    #直接查询数据,查询最后一个交易日的所有股票信息
    df=pd.read_sql('''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
    , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
    , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额 
     from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code 
     where sd.trade_date=(select trade_date from stocksdaily order by trade_date desc limit 1)''',con=engine)
    df_up=df[df['涨跌']>=0]
    df_up.sort_values('涨跌',ascending=False,inplace=True)
    df_down=df[df['涨跌']<0]
    df_down.sort_values('涨跌',ascending=True,inplace=True)
    stock={'stocks_up':df_up.iterrows(),'stocks_down':df_down.iterrows(),'stock_columns':df.columns,'stocks_up_count':df_up.shape[0],'stocks_down_count':df_down.shape[0]}
    datadic={'title':'股票信息','now':datetime.now().strftime('%y年%m月%d日%H时%M分%S秒'),'stocks':stock}
    return render(request,'stockmonitor/stocklastday.html',context=datadic)


def stocklist(request):
    sql='select * from stocklist'
    df=pd.read_sql(sql,con=engine)
    datadic={'stocklist':df.iterrows(),'stock_count':df.shape[0]}
    return render(request,'stockmonitor/stocklist.html',context=datadic)

def stock(request,ts_code):
    sql='''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
    , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
    , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额 
     from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code where sl.ts_code="{}" order by sd.trade_date desc'''.format(ts_code)
    df=pd.read_sql(sql,con=engine)
    stocks={'stocks':df.iterrows(),'stock_columns':df.columns,'stock_count':df.shape[0]}
    datadic={'stocks':stocks}
    return render(request,'stockmonitor/stock.html',context=datadic)