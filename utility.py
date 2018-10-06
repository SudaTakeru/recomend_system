# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:18:18 2018

@author: buryu-
"""

import csv
import numpy as np

def read_data(file_name):
    # ファイルからデータの読み込み
    length = len(open(file_name).readlines()) #ファイルの長さを取得
    userid=[0 for i in range(length)]
    movieid=[0 for i in range(length)]
    rating=[0 for i in range(length)]
    timestamp=[0 for i in range(length)]
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばす
        i=0
        for row in reader:
            userid[i] = int(row[0])
            movieid[i] = int(row[1])
            rating[i] = float(row[2])
            timestamp[i] = float(row[3])        
            i += 1
       
    userid = modify_id(userid)[0]
    movieid = modify_id(movieid)[0]
    rating = np.array(rating)
    timestamp = np.array(timestamp)
    
    return [userid,movieid,rating,timestamp]

def modify_id(ids):
    # 欠番を飛ばしidを付けなおす
    idset=[]
    c=0
    new_id = [0 for i in range(len(ids))]
    for i in range(len(ids)):
        if ids[i] not in idset:
            idset.append(ids[i])
            new_id[i]=c
            c += 1
        else:
            new_id[i] = idset.index(ids[i])    
    return [np.array(new_id),idset]

def map_id(ids,idset):
    # modifyしたidにidを合わせる
    # idsetにない新しいidはすべて同じidをつける
    new_id = [len(idset) for i in range(len(ids))]
    for i in range(len(ids)):
        if ids[i] in idset:
            new_id[i] = idset.index(ids[i])
    
    return np.array(new_id)
    

def divide_data(data,timerange,userrange):
    # ある時間、あるユーザーの範囲にデータを絞る　（メモリが足りなくなるため）
    # data: [userid,movieid,rating,timestamp]
    # timerange,userange: [a,b]
    d_data = [0 for i in range(4)]
    pid = np.where((data[3]>= timerange[0])&(data[3] < timerange[1])&(data[0] >= userrange[0])&(data[0] < userrange[1]))
    
    d_data[0] = data[0][pid]
    d_data[1] = data[1][pid]
    d_data[2] = data[2][pid]
    d_data[3] = data[3][pid]
    return d_data
    
def make_matrix(data):
    # users\movies Matricsを作る
    # data: [userid,movieid,rating,timestamp]
    movienum = max(data[1])+1 #映画の数を取得
    usernum = max(data[0])+1#ユーザーの数を取得
    Matrix = np.zeros((usernum,movienum))
    RateMatrix = np.zeros((usernum,movienum))   

    for i in range(max(data[0])+1):
        # マトリックスを作成
        userind = np.where(data[0] == i)
        movieind = data[1][userind] 
        Matrix[i,movieind] = 1
        RateMatrix[i,movieind] = data[2][userind]
    
    return [Matrix,RateMatrix]
    
def precision(a,b):
    # presicionを算出
    # a is true matrix
    # b is recomend matrix
    usernum = a.shape[0]
    pos = []
    v = 0
    for i in range(usernum):
        recomend_num = np.sum(b[i,:])
        re_pe_num = np.sum((b[i,:]==1)&(a[i,:]==1))
        if recomend_num >0:
            v += float(re_pe_num)/float(recomend_num)
            pos.append([i])
    if len(pos)>0:
        v = v/float(len(pos))
    
    return v 

def recall(a,b):
    # presicionを算出
    # a is true matrix
    # b is recomend matrix
    usernum = a.shape[0]
    pos = []
    v = 0
    for i in range(usernum):
        purchase_num = np.sum(a[i,:])
        re_pe_num = np.sum((b[i,:]==1)&(a[i,:]==1))
        if purchase_num >0:
            v += float(re_pe_num)/float(purchase_num)
            pos.append([i])
    if len(pos)>0:
        v = v/float(len(pos))
        
    return v 