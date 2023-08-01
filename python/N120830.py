def solution(n: int, k: int) -> int:
    n_price= 12000
    k_price= 2000

    free_k= n // 10
    return (n*n_price)+((k-free_k) *k_price)

print(solution(10,3))
