def solution(cipher: str, code: int):
    answer= ""

    for i,c in enumerate(cipher):
        if ((i+1) % code) == 0:
            answer+=c 
    return answer

print(solution("dfjardstddetckdaccccdegk", 4))
