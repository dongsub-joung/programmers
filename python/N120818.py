# https://dingx2-story.tistory.com/50
# test 13,14 case fail

def solution(price: int):
    answer= 0
    if price >= 500000:
        answer= price * 0.8
    elif price >= 300000:
        answer= price * 0.90
    elif price >= 100000:
        answer= price * 0.95
    else:
        answer= price
    return int(answer)
