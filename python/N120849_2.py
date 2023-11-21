def solution(my_string):
    answer = ''
    listUp= ("a,e,i,o,u")

    for c in my_string:
        if c not in listUp:
            answer+= c

    return answer
