def solution(arr: list, n: int):
    box= []
    arr.sort()
    for i in arr:
        box.append(abs(n-i))
    answer= [arr[box.index(min(box))]]
    if len(answer)> 1:
        return min(answer)
    else:
        return answer[0]


# my code
def solution2(arr: list, n: int):
    minues=[]
    for number in arr:
         minues.append(abs(number - n))

    mini= 101
    for i in minues:
        if mini > i:
            mini= i
    
    answer= minues.index(mini)

    return arr[answer]


print(solution([3, 10, 28], 20))
