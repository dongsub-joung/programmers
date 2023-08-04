
def solution(letter: str)->str:
    letters= list(letter.split(" "))
    mos= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    nums= [chr(x+97) for x in range(26)]
    answer = ''
    
    for e in letters:
        idx= mos.index(e)
        answer+= nums[idx]
    
    return answer

print(solution(".... . .-.. .-.. ---"))