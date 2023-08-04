def solution(rsp:str)->str:
    if len(rsp) == 1:
        if rsp == "2":
            return "0"
        elif rsp == "0":
            return "5"
        elif rsp == "5":
            return "2"
    
    buff= ""
    for c in rsp:
        if c == "2":
            buff+= "0"
        elif c == "0":
            buff+= "5"
        elif c == "5":
            buff+= "2"

    return buff

print(solution("205"))