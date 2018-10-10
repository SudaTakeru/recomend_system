# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:30:52 2018

@author: buryu-
"""
import numpy as np
from numpy import linalg as LA

class Lossfunction:
    # r,x,y:numpy array
    # r = (n,k)
    # x = (n,f)
    # y = (f,k)
    # Lambda is  regularizing parameter
    
    def __init__(self,r,Lambda):
        self.r=r
        self.l=Lambda
        maskid = self.r > 0
        self.mask = np.zeros(self.r.shape)
        self.mask[maskid] = 1
        
    def loss(self,x,y):
        x = np.array(x)
        y = np.array(y)
        temp = np.square(self.r - np.dot(x,y)) 
        reg = np.sum(self.l*(LA.norm(x,axis=0)))+np.sum(self.l*(LA.norm(y,axis=1)))
        temp = temp * self.mask
        loss=np.sum(temp,axis=(0,1)) + reg
        return loss