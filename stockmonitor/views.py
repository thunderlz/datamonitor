from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
from django.core.paginator import Paginator

engine = create_engine(
    'mysql+pymysql://root:751982leizhen@localhost:3306/leizquant')


# Create your views here.

# 老的昨日交易数据路由函数
# def stocklastday(request):
#     # 直接查询数据,查询最后一个交易日的所有股票信息
#     df = pd.read_sql('''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
#     , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
#     , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额
#      from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code
#      where sd.trade_date=(select trade_date from stocksdaily order by trade_date desc limit 1)''', con=engine)
#     df_up = df[df['涨跌'] >= 0]
#     df_up.sort_values('涨跌', ascending=False, inplace=True)
#     df_down = df[df['涨跌'] < 0]
#     df_down.sort_values('涨跌', ascending=True, inplace=True)
#     stock = {'stocks_up': df_up.iterrows(), 'stocks_down': df_down.iterrows(), 'stock_columns': df.columns,
#              'stocks_up_count': df_up.shape[0], 'stocks_down_count': df_down.shape[0]}
#     datadic = {'title': '股票信息', 'now': datetime.now().strftime(
#         '%y年%m月%d日%H时%M分%S秒'), 'stocks': stock}
#     return render(request, 'stockmonitor/stocklastday.html', context=datadic)


# 根据涨跌不同显示
def stocklastday(request, updown):
    # 直接查询数据,查询最后一个交易日的所有股票信息
    global df
    if request.GET.get('page') == None:
        if updown == 'up':
            df = pd.read_sql('''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
            , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
            , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额 
            from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code 
            where sd.trade_date=(select trade_date from stocksdaily order by trade_date desc limit 1) and sd.pct_chg>=0''', con=engine)
        else:
            df = pd.read_sql('''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
            , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
            , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额 
            from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code 
            where sd.trade_date=(select trade_date from stocksdaily order by trade_date desc limit 1) and sd.pct_chg<0''', con=engine)
        df.sort_values('涨跌', ascending=True, inplace=True)
    
    df_pages = Paginator(df, 50)
    df_page = df_pages.get_page(request.GET.get('page'))
    if updown == 'up':
        df_up = df_page.object_list
        stock = {'stocks_up': df_up.iterrows(), 'stock_columns': df.columns,
                 'stocks_up_count': df.shape[0]}
    else:
        df_down = df_page.object_list
        stock = {'stocks_down': df_down.iterrows(), 'stock_columns': df.columns,
                 'stocks_down_count': df.shape[0]}

    datadic = {'title': '股票信息', 'now': datetime.now().strftime(
        '%y年%m月%d日%H时%M分%S秒'), 'stocks': stock, 'page_obj': df_page}
    return render(request, 'stockmonitor/stocklastday.html', context=datadic)


def stocklist(request):

    sql = 'select * from stocklist'
    df = pd.read_sql(sql, con=engine)
    dfsl_pages = Paginator(df, 100)
    dfsl_page = dfsl_pages.get_page(request.GET.get('page'))
    df_sl = dfsl_page.object_list
    datadic = {'page_obj': dfsl_page, 'stocklist': df_sl.iterrows(),
               'stock_count': df.shape[0]}
    return render(request, 'stockmonitor/stocklist.html', context=datadic)


def stock(request, ts_code, page):
    global dfstock_pages
    if page == 1:
        sql = '''select sd.ts_code 股票代码, sl.name 股票名称 , sl.area 区域 , sl.industry 行业 , sl.list_date 挂牌时间
        , sd.trade_date 交易日期 , sd.openprice 开盘价 , sd.highprice 最高价 , sd.lowprice 最低价 , sd.closeprice 收盘价
        , sd.pre_closeprice 前一交易日收盘价 , sd.changeprice 涨跌价 , sd.pct_chg 涨跌 , sd.vol 交易量 , sd.amount 交易额 
            from stocksdaily sd left join stocklist sl on sd.ts_code = sl.ts_code where sl.ts_code="{}" order by sd.trade_date desc'''.format(ts_code)
        df = pd.read_sql(sql, con=engine)
        dfstock_pages = Paginator(df, 50)
    dfstock_page = dfstock_pages.get_page(page)
    df_stock = dfstock_page.object_list
    # print(dfstock.page.)
    stock = {'page_obj': dfstock_page, 'stock': df_stock.iterrows(), 'stock_columns': df_stock.columns,
             'stock_count': df_stock.shape[0], 'ts_code': ts_code}
    datadic = {'stock': stock}
    return render(request, 'stockmonitor/stock.html', context=datadic)
