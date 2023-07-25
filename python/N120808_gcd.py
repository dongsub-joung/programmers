def solution(denum1, num1, denum2, num2):
    boonmo= num1 * num2
    boonja= denum1 * num2 + denum2 *num1

    start= max(boonmo, boonja)
    gcd_Value= 1

    for num in range(start, 0, -1):
        if boonmo % num == 0 and boonja % num == 0:
            gcd_Value= num
            break

    return [boonja / gcd_value, boonmo / gcd_Value]