def solution(numbers: str):
    answer= 0
    str_numbers= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for idx, num in enumerate(str_numbers):
        numbers= numbers.replace(num, str(idx))

    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))
