# -*- coding:utf-8 -*-
# 模仿

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import schedule2016 as schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-09-09'
span = 5
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
            for i in range(len(data)):
                # print ''
                # print data[i]['inc'],data[i+1]['inc']
                if (data[i+1]['vol']/data[i]['vol'])>3:
                    if (data[i+1]['high']-data[i+1]['low'])/abs(data[i+1]['open']-data[i+1]['close'])>5:
                        count += 1
                        print ''
                        print 'No.', count
                        print 'turnover:', data[i+1]['turnover']
                        print data[i+1]['tick'],data[i+1]['dt']
                        print ('----------------')
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
