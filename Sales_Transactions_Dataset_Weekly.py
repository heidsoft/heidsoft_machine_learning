#!/usr/bin/pytthon
# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt

filename='Sales_Transactions_Dataset_Weekly.csv'
W0=[]
with open(filename) as f:
       reader=csv.reader(f)
       header_row=next(reader)
       print header_row
       for row in reader:
       	w0=int(row[1])
       	W0.append(w0)

print  W0  

names = [u'张',u'李',u'赵']
x = range(len(names))
plt.plot(x,[100,200,300])
plt.xticks(x,names,rotation=45)
plt.title(u"销售数据",fontsize=24)
plt.xlabel(u'产品编号',fontsize=16)
plt.ylabel(u'销售数量',fontsize=16)

plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()