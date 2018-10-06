# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:55:14 2018

@author: buryu-
"""

import numpy as np
import matplotlib.pyplot as plt
from lossfunction import Lossfunction 
from NeighborCF import NeighborCF
from utility import *

a = 60*60*24*7*20 #最新dataのから20週間前から
b = 60*60*24*7*2 #最新dataの2週間前まで

usernum0 = 610 #データを用いるユーザーの数
reuser = 4 # レコメンドするユーザーの数

threshold = 0.1 #推薦する評価値の閾値

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

# CF
NCF = NeighborCF(Matrixs[0])

rhat = np.zeros((reuser,Matrixs[0].shape[1]))
for i in range(reuser):
    rhat[i,:] = NCF.recomend(i)


# 推薦するアイテムをユーザー毎に決定する
pos = np.where(rhat >= threshold)
r = np.zeros(rhat.shape)
r[pos]=1
r = r - Matrixs[0][:reuser,:]
 
#評価に用いるdata（最新dataの2週間前から最新dataまで）のMatrixを準備
userrange=[0,usernum0]
timerange=[max(data0[3])-b,max(data0[3])]
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
pre = precision(tMatrixs[0][:reuser,:],r)
# Recall
rec = recall(tMatrixs[0][:reuser,:],r)
print('precision : '+str(pre))
print('recall : '+str(rec))


