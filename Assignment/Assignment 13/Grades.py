##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 13
##
##########################################

import math
import statistics

def total(values : list) -> float:
    list_total = 0
    for nums in values:
        list_total += nums
    return list_total

def average(values : list) -> float:
    if len(values) == 0:
        return math.nan
    avg = sum(values)/len(values)
    return avg

def median(values : list) -> float:
    values.sort()
    new_values = statistics.median(values)

    '''m = len(values)
    if m % 2 == 0:
        med1 = values[m//2]
        med2 = values[m//2 - 1]
        med = (med1 + med2) / 2
    else:
        med = values[m//2]'''
        #tries this first but gave an error so I researched a new way to calculate median with python 3.0
    return new_values



#print(total([4, 2, 5]))
#print(average([2, 5, 9]))
#print(median([2, 5, 1, 3]))