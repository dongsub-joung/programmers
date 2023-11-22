def solution(s: str):
    stack= []
    for n in s.split(' '):
        try: 
            stack.append(int(n))
        except:
            stack.pop()
    return sum(stack)

print(solution("1 2 Z 3"))
print(solution("10 Z 20 Z 1"))
