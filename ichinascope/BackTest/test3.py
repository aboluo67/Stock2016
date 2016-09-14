# -*- coding:utf-8 -*-
# 金叉 ：3日内MACD DIFF DEA 均小于0 MACD下于0.1
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
datalist = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2015
start = '2015-07-01'
span = 10

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)

count = 0
ticklen = len(tick.tick)

for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            if data[0]['low']>data[-1]['low']:
                if data[-1]['high']>data[-2]['high']:
                    if data[-1]['high']>data[-3]['high']:
                        if data[-1]['high']>data[-4]['high']:
                            print 'ZZZ'
                            if data[-1]['high']>data[-5]['high']:
                                if data[-1]['high']>data[-6]['high']:
                                    if data[-1]['high']>data[-7]['high']:
                                        if data[-1]['high']>data[-8]['high']:
                                            # if data[-1]['high']>data[-9]['high']:
                                                count += 1
                                                print('')
                                                print 'No. ',count
                                                print data[0]['tick'],data[0]['dt']
                                                print '----------------'
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()