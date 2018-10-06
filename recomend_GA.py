# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:15:06 2018

@author: buryu-
"""

import numpy as np
import matplotlib.pyplot as plt
from lossfunction import Lossfunction 
from GA import GA
from utility import *

a = 60*60*24*7*3 #最新dataのから3週間前から
b = 60*60*24*7*2 #最新dataの2週間前まで
c = 60*60*24*7*1
usernum0 = 610 #データを用いるユーザーの数

threshold = 0.8 #推薦する評価値の閾値

## ファイル読み込み
file_name='ml-latest-small/ratings.csv'

data0 = read_data(file_name)

#用いるdataを絞る
userrange=[0,usernum0]
timerange=[max(data0[3])-a,max(data0[3])-b]
data = divide_data(data0,timerange,userrange)

# idを付けなおす
[data[0],user_idset] = modify_id(data[0]) 
[data[1],item_idset] = modify_id(data[1]) 

Matrixs = make_matrix(data)

# Latent factor models
# 遺伝的アルゴリズムによる最適化
f=30 #facterの数
time = 100 #トレーニング回数
node = 50 #ganeの数

usernum=Matrixs[0].shape[0]
itemnum=Matrixs[0].shape[1]

Lambda=0.1
lo=Lossfunction(Matrixs[0],Lambda)

ga = GA(lo,node)
ranges = [-10,10] #初期値の値の範囲
print('training_start')
ga.random_initilize([usernum,f],[f,itemnum],ranges,ranges)
[x,y,loss]=ga.training(time,v=2)
print('loss : '+str(loss[-1]))

# 評価値を算出
rhat=np.dot(x,y)

# 推薦するアイテムをユーザー毎に決定する
pos = np.where(rhat >= threshold)
r = np.zeros(rhat.shape)
r[pos]=1
r = r - Matrixs[0]
 
#評価に用いるdata（最新dataの2週間前から1週間前まで）を準備
userrange=[0,usernum0]
timerange=[max(data0[3])-b,max(data0[3]-c)]
tdata = divide_data(data0,timerange,userrange)

tdata[0] = map_id(tdata[0],user_idset)
tdata[1] = map_id(tdata[1],item_idset)
tMatrixs = make_matrix(tdata)
if tMatrixs[0].shape[0]>Matrixs[0].shape[0]:
    tMatrixs[0]=tMatrixs[0][:-1,:]
if tMatrixs[0].shape[1]>Matrixs[0].shape[1]:
    tMatrixs[0]=tMatrixs[0][:,:-1]
#評価
# Precision
pre = precision(tMatrixs[0],r)
# Recall
rec = recall(tMatrixs[0],r)
print('precision : '+str(pre))
print('recall : '+str(rec))


