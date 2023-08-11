def solution(hp: int)->int:
    answer = 0
    attacker= [5,3,1]
    cnt= []
    while hp != 0:   
        cnt.append(hp // attacker[0])
        hp%= attacker[0]
        

        cnt.append(hp // attacker[1])
        hp%= attacker[1]

        cnt.append(hp)
        hp-=hp
        answer= sum(cnt)
    return answer
