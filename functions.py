#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:11:10 2023

@author: kaandural
"""

def get_unique_list_f(lst):
    new_list = set(lst)
    list_2 = list(new_list)
    return list_2
#list_a = [1,2,3,3,3,3,4,5]
#get_unique_list(list_a)
def count_case_f(string):
    lower = 0
    upper = 0

    for i in string: 
        if (i.islower()):
            lower += 1
            
        if (i.isupper()):
                upper += 1
                
    
    return(upper,lower)
    
x = ("Hello World")
#count_case(x)
import string

def remove_punctuation_f(sentence):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    clean = " "

    for i in sentence:
        if i not in punc:
            clean += i
    return clean
        
def word_count_f(sentence):
    counts = ()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
import functions