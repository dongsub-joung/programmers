def solution(num_list: list, n: int)->list:
    ans, temp= [], []
    cnt= 0

    for num in num_list:
        temp.append(num)
        cnt+=1

        if cnt == n:
            ans.append(temp)
            temp.clear()
            cnt=0
    return ans

# out of range: j
def solution2(num_list: list, n: int)->list:
    size= len(num_list) // n
    i,j= 0,0
    answer = [[0 for _ in range(n)] for _ in range(size)]

    for e in num_list:
        answer[i][j]= e
        if i % 2 ==0:
            i+=1
        j+=1

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))