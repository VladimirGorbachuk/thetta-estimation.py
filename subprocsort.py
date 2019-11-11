# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:37:04 2019

@author: Vovan-i-Venera
"""

numbers = [int(number) for number in input().split()]
numbers = sorted(numbers)
print(*numbers)