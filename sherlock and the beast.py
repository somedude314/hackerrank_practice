#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())


def printsol(y):
    if y == 1:
        for i in range (0,num):
            print('5', end='')
        print()
    elif y == 2:
        for i in range (0,num):
            print('3', end='')
        print()
def printsol2(num, x):
    for i in range(0, num-x):
        print('5', end='')
    for i in range (0,x):
        print('3', end='')


numbers = int(input())


for i in range(0,numbers):
    flag = 0
    num = int(input())
    x = num %3
    if x == 0:
        printsol(1)
        flag = 1
    else:
        while x < num:
            if(x) % 5 == 0:
                printsol2(num,x)
                flag = 1
                break
            else:
                x = x + 3
    if(flag != 1):
        if num%5 == 0:
            printsol(2)
        else:
            print(-1)