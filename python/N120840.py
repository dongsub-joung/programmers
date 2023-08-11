import math

def solution(balls, share):
    answer = 0
    upper= math.factorial(balls)
    lower= math.factorial(balls-share) * math.factorial(share)
    answer= upper // lower
    return answer
