# -*- coding:utf-8 -*-
# 长下影线
# 20160912暴跌  选出长下影线的 观察

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-09-12'
span = 2
data = []
datalist = []

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print time.strftime("%Y-%m-%d", time.localtime())


datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)
count = 0
ticklen = len(tick.tick)

#300431 2016-06-13

for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i], 'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            if data[0]['open']>data[0]['close']:
                if ((data[0]['close']-data[0]['low'])/(data[0]['open']-data[0]['close']))>2:
                    if data[0] != [] and data[1] != []:
                        count += 1
                        print ''
                        print 'No.',count
                        print 'Num:', round(((data[0]['close']-data[0]['low'])/(data[0]['open']-data[0]['close'])),1)
                        print 'inc:', data[1]['inc']
                        print data[0]['tick'],data[0]['dt']
                        print ('----------------')
            if data[0]['open']<data[0]['close']:
                if ((data[0]['open']-data[0]['low'])/(data[0]['close']-data[0]['open']))>2:
                    if data[0] != [] and data[1] != []:
                        count += 1
                        print ''
                        print 'No.', count
                        print 'Num:', round(((data[0]['open']-data[0]['low'])/(data[0]['close']-data[0]['open'])),1)
                        print 'inc:', data[1]['inc']
                        print data[0]['tick'],data[0]['dt']
                        print ('----------------')
        except:print EOFError
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
