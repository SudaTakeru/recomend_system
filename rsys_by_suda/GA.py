# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:13:56 2018

@author: buryu-
"""
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import animation

class GA:
    # function : loss function class
    # time : iteration times
    # nodes : number of survive gane
    def __init__(self,function,nodes):
        self.fn = function
        self.n = nodes
        
    def random_initilize(self,x_shape,y_shape,x_range,y_range):
        # x_range and y_range : [a,b]
        # ランダムに初期化
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.xs=[x_range[0]+(x_range[1]-x_range[0])*np.random.rand(x_shape[0],x_shape[1]) for i in range(self.n)]
        self.ys=[y_range[0]+(y_range[1]-y_range[0])*np.random.rand(y_shape[0],y_shape[1]) for i in range(self.n)]
        
    
    def training(self,time,v=1,d=0):
        # トレーニング
        self.time = time # トレーニング回数
        minlosses = [0 for i in range(self.time)]
        ims=[]
        if v==1 and d==2:
            fig = plt.figure()
            im = plt.scatter(self.xs, self.ys)
            ims.append(im)
        for i in range(self.time):
            if d==2:
                self.crossover_2d()
            else:
                self.crossover()
            losses=self.survive()
            minlosses[i]=losses[0]
            
            if v==1 and d==2:
                print('times '+str(i)+': '+str(losses[0]))
                im = plt.scatter(self.xs, self.ys)
                ims.append(im)
            elif v==2:
                print('times '+str(i)+': '+str(losses[0]))
        if v==1 and d==2:
            ani = animation.ArtistAnimation(fig, ims)
            ani.save('training.gif', writer='imagemagick')
        
        return [self.xs[0],self.ys[0],minlosses]
        
    def crossover_2d(self):
        # 交配　2次元
        childrenx=[]
        childreny=[]
        for i in range(int(self.n/2.0)):
            fi = np.random.randint(self.n)
            mi = np.random.randint(self.n)
            #sigmax = 0.5*LA.norm(np.array(self.xs[fi])-np.array(self.xs[mi]),axis=0)
            meanx = (np.array(self.xs[fi][0][0])-np.array(self.xs[mi][0][0]))/2
            #sigmay = 0.5*LA.norm(np.array(self.ys[fi])-np.array(self.ys[mi]),axis=0)
            meany = (np.array(self.ys[fi][0][0])-np.array(self.ys[mi][0][0]))/2
            covM = np.cov(np.array([[self.xs[fi][0][0],self.ys[fi][0][0]],
                                    [self.xs[mi][0][0],self.ys[mi][0][0]]]))
            child = np.random.multivariate_normal([meanx,meany],covM)
            childx = np.array([[child[0]]])#np.random.normal(meanx,sigmax)
            childrenx.append(childx)
            childy = np.array([[child[1]]])#np.random.normal(meany,sigmay)
            childreny.append(childy)
            
        self.xs.extend(childrenx)
        self.ys.extend(childreny)
        
    def crossover(self):
        # 交配
        childrenx=[]
        childreny=[]
        for i in range(int(self.n/2.0)):
            fi = np.random.randint(self.n)
            mi = np.random.randint(self.n)
            temp1 = np.concatenate([np.array(self.xs[fi]).reshape(self.x_shape[0]*self.x_shape[1],),np.array(self.ys[fi]).reshape(self.y_shape[0]*self.y_shape[1],)])
            temp2 = np.concatenate([np.array(self.xs[mi]).reshape(self.x_shape[0]*self.x_shape[1],),np.array(self.ys[mi]).reshape(self.y_shape[0]*self.y_shape[1],)])
            covM = np.cov(np.array([temp1,temp2]).transpose())
            mean = temp1-temp2
            child = np.random.multivariate_normal(mean,covM)
            childx = child[:self.x_shape[0]*self.x_shape[1]].reshape((self.x_shape[0],self.x_shape[1]))
            childrenx.append(childx)
            childy = child[self.x_shape[0]*self.x_shape[1]:].reshape((self.y_shape[0],self.y_shape[1]))
            childreny.append(childy)
            
        self.xs.extend(childrenx)
        self.ys.extend(childreny)
        
    def survive(self):
        # 値の良い上位ｎ個を選ぶ
        losses = [10**5 for i in range(len(self.xs))]
        for i in range(len(self.xs)):
            losses[i]=self.fn.loss(self.xs[i],self.ys[i])
        sid = np.argsort(np.array(losses))
        sid = sid[:self.n]
        self.xs = np.array(self.xs)[sid].tolist()
        self.ys = np.array(self.ys)[sid].tolist()
        return np.array(losses)[sid].tolist()
    
        
