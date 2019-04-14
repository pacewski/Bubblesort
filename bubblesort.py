# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:42:00 2019

@author: pacew
"""

# A bubble sort app


import numpy as np
import random


def bubblesort(array):
    lenght = len(array) - 1
    for i in range(lenght):
        for j in range(lenght):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array 


x = int(input("how long shout the array be? \n"))
randnums = np.random.randint(1, 101, x)
print("the array of numbers to sort is:")
print(randnums)
array = randnums
print("sorted array by bubble sort method:")
print(bubblesort(array))

