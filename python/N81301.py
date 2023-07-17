# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
# 숫자 문자열과 영단어 

# Its not work
def solution(s):
    answer = ""
    buff= []

    for e in s:
        if chr(e) < 97:
            answer+= e
        else:
            str_buff= ""
            str_buff+= e
            if len(buff) >= 3:
                buff.append(str_buff)
    return answer

# https://velog.io/@jerry_bak/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC-%EC%98%81%EB%8B%A8%EC%96%B4-python
def solution2(s: str):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, c in enumerate(arr):
        s= s.replace(c, str(i))
    return int(s)