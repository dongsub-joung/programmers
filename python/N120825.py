def solution(my_string, n):
    answer = ''
    for e in my_string:
        answer+= e * n
    return answer
