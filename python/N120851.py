def solution(string: str):
    answer= 0
    for c in string:
        try:
            number= int(c)
        except:
            continue
        answer+= number
    
    return answer
