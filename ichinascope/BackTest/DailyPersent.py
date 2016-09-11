# -*- coding:utf-8 -*-
# 每日个股占的百分比
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import schedule2014 as schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2014
start = '2014-08-08'
span = 1
data = []
datalist = []

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

datalistindex = schedule.schedule.index(start)

countall = 0
countp0 = 0
countm0 = 0
countp1 = 0
countm1 = 0
countp2 = 0
countm2 = 0
countp3 = 0
countm3 = 0
countp4 = 0
countm4 = 0
countp5 = 0
countm5 = 0
countp6 = 0
countm6 = 0
countp7 = 0
countm7 = 0
countp8 = 0
countm8 = 0
countp9 = 0
countm9 = 0
countp10 = 0
countm10 = 0

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)
print datalist[0],' to ',datalist[-1]

ticklen = len(tick.tick)

for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i], 'tick':ticki}):
            data.append(item)
    for i in range(len(data)):
        countall += 1
        if 0 <= data[i]['inc'] <= 1:
            countp0 += 1
        if 1 <= data[i]['inc'] <= 2:
            countp1 += 1
        if 2 <= data[i]['inc'] <= 3:
            countp2 += 1
        if 3 <= data[i]['inc'] <= 4:
            countp3 += 1
        if 4 <= data[i]['inc'] <= 5:
            countp4 += 1
        if 5 <= data[i]['inc'] <= 6:
            countp5 += 1
        if 6 <= data[i]['inc'] <= 7:
            countp6 += 1
        if 7 <= data[i]['inc'] <= 8:
            countp7 += 1
        if 8 <= data[i]['inc'] <= 9:
            countp8 += 1
        if 9 <= data[i]['inc'] < 10:
            countp9 += 1
        if 9.9 <= data[i]['inc'] < 11:
            countp10 += 1
        if -1 <= data[i]['inc'] <= 0:
            countm0 += 1
        if -2 <= data[i]['inc'] <= -1:
            countm1 += 1
        if -3 <= data[i]['inc'] <= -2:
            countm2 += 1
        if -4 <= data[i]['inc'] <= -3:
            countm3 += 1
        if -5 <= data[i]['inc'] <= -4:
            countm4 += 1
        if -6 <= data[i]['inc'] <= -5:
            countm5 += 1
        if -7 <= data[i]['inc'] <= -6:
            countm6 += 1
        if -8 <= data[i]['inc'] <= -7:
            countm7 += 1
        if -9 <= data[i]['inc'] <= -8:
            countm8 += 1
        if -11 <= data[i]['inc'] <= -9:
            countm9 += 1
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
print ''
print '+0.X ','%3d' % countp0,' ','%3.3f' % round(countp0*1.0/countall,3)
print '+1.X ','%3d' % countp1,' ','%3.3f' % round(countp1*1.0/countall,3)
print '+2.X ','%3d' % countp2,' ','%3.3f' % round(countp2*1.0/countall,3)
print '+3.X ','%3d' % countp3,' ','%3.3f' % round(countp3*1.0/countall,3)
print '+4.X ','%3d' % countp4,' ','%3.3f' % round(countp4*1.0/countall,3)
print '+5.X ','%3d' % countp5,' ','%3.3f' % round(countp5*1.0/countall,3)
print '+6.X ','%3d' % countp6,' ','%3.3f' % round(countp6*1.0/countall,3)
print '+7.X ','%3d' % countp7,' ','%3.3f' % round(countp7*1.0/countall,3)
print '+8.X ','%3d' % countp8,' ','%3.3f' % round(countp8*1.0/countall,3)
print '+9.X ','%3d' % countp9,' ','%3.3f' % round(countp9*1.0/countall,3)
print '+10.X ','%3d' % countp10,' ','%3.3f' % round(countp10*1.0/countall,3)
print '-0.X ','%3d' % countm0,' ','%3.3f' % round(countm0*1.0/countall,3)
print '-1.X ','%3d' % countm1,' ','%3.3f' % round(countm1*1.0/countall,3)
print '-2.X ','%3d' % countm2,' ','%3.3f' % round(countm2*1.0/countall,3)
print '-3.X ','%3d' % countm3,' ','%3.3f' % round(countm3*1.0/countall,3)
print '-4.X ','%3d' % countm4,' ','%3.3f' % round(countm4*1.0/countall,3)
print '-5.X ','%3d' % countm5,' ','%3.3f' % round(countm5*1.0/countall,3)
print '-6.X ','%3d' % countm6,' ','%3.3f' % round(countm6*1.0/countall,3)
print '-7.X ','%3d' % countm7,' ','%3.3f' % round(countm7*1.0/countall,3)
print '-8.X ','%3d' % countm8,' ','%3.3f' % round(countm8*1.0/countall,3)
print '-9.X ','%3d' % countm9,' ','%3.3f' % round(countm9*1.0/countall,3)
