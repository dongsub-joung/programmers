# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 짝수는 싫어요

def isOdd(n):
    if n % 2 != 0:
        return n
    else:
        pass

n= int(input())
answer= [i for i in range(n+1) if isOdd(i)]
print(answer) 