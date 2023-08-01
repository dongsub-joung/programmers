def solution(n: int)->int:
    answer = 0
    for e in range(1, n+1):
        if e % 2 == 0:
            answer+= e
    return answer
