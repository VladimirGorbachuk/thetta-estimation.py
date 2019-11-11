# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:44:35 2019

@author: Vovan-i-Venera
"""
numbers = [int(number) for number in input().split()]
n = 1
while n < len(numbers):
   for i in range(len(numbers) - n):
       if numbers[i] > numbers[i + 1]:
           numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
   n += 1
print(*numbers)