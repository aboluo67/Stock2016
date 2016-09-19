# -*- coding:utf-8 -*-
# 立庄量
# 参考000014 2016-07-26
# 前期先缩量 再放量下跌 说明已有散户割肉 再缩量 到地量 可买入

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
start = '2016-04-18'
span = 108
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



for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i], 'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            for i in range(len(data)-5):
                if data[i]['vol']>data[i+1]['vol'] and (data[i+2]['vol']/data[i+1]['vol'])>2.5:
                    if data[i + 5]['high'] > data[i + 4]['high'] > data[i + 3]['high']:
                        if data[i + 5]['low'] > data[i + 4]['low'] > data[i + 3]['low']:
                            count += 1
                            print ''
                            print 'No.', count
                            print 'turnover:', data[i+2]['turnover']
                            print data[i]['tick'],data[i]['dt']
                            print ('----------------')
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
