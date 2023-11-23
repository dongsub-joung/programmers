def solution(order: int):
    answer= 0
    clap= ['3', '6', '9']
    for c in str(order):
        if c in clap:
            answer+= 1
    return answer


print(solution(29423))
