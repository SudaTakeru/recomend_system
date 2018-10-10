# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:21:09 2018

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
    
    def __init__(self,Lambda):
        self.l=Lambda
        
    def loss(self,x,y):
        one = np.ones(np.array(x).shape)
        x = np.array(x)
        y = np.array(y)
        temp = np.sqrt(np.dot(np.transpose(x+one),x+one))+np.sqrt(np.dot(np.transpose(y),y)) 
        loss=np.sum(temp,axis=(0,1))
        return loss