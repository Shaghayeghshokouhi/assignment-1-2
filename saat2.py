# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:00:35 2023

@author: 2022
"""

class time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    def sum (self,t):
        h= self.h + t.h
        m= self.m + t.m
        s= self.s + t.s
        if s >= 60:
            m += 1
        if m >= 60:
            h += 1
            result = time(h, m, s):
            return result
    def sub(self, t):
        h = self.h - t.h
        m = self.m - t.m
        s = self.s - t.s
        if m < 0:
            m += 60
            h -= 1
        result = time(h,m,s)
        return result
    def second(self,s):
        self.s = s
        self.m = m
        self.h = h
        return time(h,m, s)
    def time_to_second(self,h, m,s):
        self.s = h*3600 + m*60
        return self.s
    def show(self):
        print(self.h : self.m : self.s)
        