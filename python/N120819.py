def solution(money: int) -> list:
    coffe= 5500
    
    cup_amount= money // coffe
    remain_money= money % coffe

    return [cup_amount, remain_money] 
