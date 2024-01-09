# 1 ~ n 까지의 합 구하기
def recur_sum(n: int) -> int:
    # 탈출조건
    if n == 0:
        return 0

    # +100 -> +99 ... -> +1 -> 0 -> 탈출시작(이후부터 덧셈시작) -> ...
    return recur_sum(n - 1) + n
    
# input
n = int(input())
result: int = recur_sum(n)
print(result)