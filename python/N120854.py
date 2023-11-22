def solution(strlist: list):
    answer= []
    for string in strlist:
        answer.append(len(string))
    return answer


print(solution(["We", "are", "the", "world!"]))
