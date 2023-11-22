def solution(my_string: str):
    answer= '';
    strList= [*my_string]
    buffList= []
    for string in strList:
        if string not in buffList:
            buffList.append(string)

    for c in buffList:
        answer+= c

    return answer

print(solution("people"))
