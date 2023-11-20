def solution(my_string):
    listUp= ("a,e,i,o,u")
    for c in listUp:
        my_string= my_string.replace(c, "")
    return my_string

print(solution("bus"))
