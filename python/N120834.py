def solution(age:int)->str:
    answer = ''
    for _ in range(len(str(age))):
        num= age % 10
        answer+= chr(97+num)
        age//= 10
    return answer[::-1]

print(solution(51))