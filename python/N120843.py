def solution(numbers: list, k: int)->int:
    return numbers[(2*(k-1)) % len(numbers)]