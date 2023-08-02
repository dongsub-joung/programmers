def solution_try1(emergency: list)->list:
    answer = []
    
    for i in range(len(emergency), 0,-1):    
        maxing= max(emergency)
        idx= emergency.index(maxing)
        answer.insert(idx, i)
        emergency.pop(idx)

    return answer

def solution(emergency: list)->list:
        

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
