def solution(n):
    answer = 0
    if n <= 7:
        return 1
    elif n % 7 ==0:
        return (n // 7)
    else:
        return (n // 7) + 1

print(solution(15))
