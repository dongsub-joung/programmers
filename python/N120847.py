def solution(numbers:list)->int:
    i, answer = 0,0
    while 1:
        muliple= numbers[i] * numbers[i+1]
        if answer <= muliple:
            answer= muliple
        i+=1
        
        if i == len(numbers)-1:
            break
    return answer

print(solution([1, 2, 3, 4, 5]))