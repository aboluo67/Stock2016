# -*- coding:utf-8 -*-
# 立庄量

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
start = '2016-05-02'
span = 50
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
            for i in range(len(data)-3):
                # print ''
                # print data[i]['inc'],data[i+1]['inc']
                if (data[i+1]['vol']/data[i]['vol'])>2.5:
                    print 'AAA'
                    if data[i + 3]['high'] > data[i + 2]['high'] > data[i + 1]['high']:
                        print 'BBB'
                        if data[i + 3]['low'] > data[i + 2]['low'] > data[i + 1]['low']:
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
