def solution(my_string: str):
    answer = []
    for c in my_string:
        try:
            c= int(c)
        except:
            continue

        if( type(c) is int):
            answer.append(c)

    answer.sort()
    return answer

print(solution("hi12392"))
