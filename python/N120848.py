from math import factorial

def solution(n:int)->int:
    k= 10
    while n < factorial(k):
        k-=1
    return k