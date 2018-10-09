# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:05:48 2018

@author: buryu-

"""
import numpy as np

class NeighborCF:
    
    def __init__(self,Matrix,t=1,k1=1):
        # ExpandedNeighbor Collaborative Filtering:t=2
        self.Matrix = Matrix
        self.type = t # ExpandedNeighbor CollaborativeFiltering or not
        self.k1=k1
        self.k2=1
        
    def recomend(self,userindex):
        s = self.get_similarity(userindex)
        sind=np.argsort(s)
        if self.type==2: # ExpandedNeighbor CollaborativeFiltering
            sl = [0 for i in range(self.k1)]
            for i in range(self.k1):
                s2 = self.get_similarity(sind[0,i])
                s2ind=np.argsort(s2)
                s2ind = s2ind[:self.k2]
                s2 = s2[:,s2ind]
                s3 = s[:,s2ind]
                sl[i] = s2+s3/2.0
            if np.sum(sl)!=0:
                r = np.dot(sl,self.Matrix[sind[:self.k1],:])/np.sum(sl)
            else:
                r=np.zeros((1,self.Matrix.shape[1]))
        else:
            s[0,userindex]=0
            s = s[:,sind[:self.k1]]
            if np.sum(s)!=0:
                r = np.dot(s,self.Matrix[sind[:self.k1],:])/np.sum(s)
            else:
                r=np.zeros((1,self.Matrix.shape[1]))
        return r
    
    def get_similarity(self,userindex):
        s = np.ones((1,self.Matrix.shape[0]))
        s = s*10**5
        for i in range(self.Matrix.shape[0]):
            if i != userindex:
                s[0,i] = self.Cos_similarity(self.Matrix[userindex,:],self.Matrix[i,:])
        return s
    
    def Cos_similarity(self,a,b):
        # a,b: ユーザーa,bの購入歴Matrix(numpyarray(n,)) n:アイテム数
        return np.sum(a*b)/np.sqrt(np.sum(a)*np.sum(b))
        
    