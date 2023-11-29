# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:00:38 2023

@author: 2022
"""

class Fraction:
    def __init__(self, s1 , m1, s2, m2):
        self.s1 = s1
        self.m1 = m1
        self.s2 = s2
        self.m2 = m2
    def sum(self):
        resul__s = s1*m2 + s2*m1
        result__m = m1* m2
        return result__s , result__m
    def mul(self):
        result__s = s1*s2
        result__m =  m1*m2
        result = Fraction(s, m)
        return result
    def sub(self):
        resul__s = s1*m2 / s2*m1
        result__m = m1* m2
        return result__s , result__m
    def div(self):
        result__s = s1*m2
        result__m = m1*s2
        return result__s / result__m
    def show(self):
        
    def fraction_to_number(s,m)
        if m1 or m2 == 0:
            return error
        else:
            result = s/m
            
f1 = Fraction(2,3)
f1.show()

f2 = fraction(4,5)
f2.show()
 print(result)
