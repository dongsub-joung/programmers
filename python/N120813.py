def solution(n):
    answer = []
    for e in range(1, n+1):
        if e % 2 == 1:
            answer.append(e)
    return answer
