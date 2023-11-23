def solution(my_string: str):
    answer= ""
    for c in my_string:
        c= ord(c)
        if c < 95:
            c+= 32
        else:
            c-= 32
        answer+= chr(c)
    return answer

print(solution("cccCCC"))
