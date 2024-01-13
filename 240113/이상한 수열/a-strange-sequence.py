def recurrance(n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    return recurrance(int(n // 3)) + recurrance(n - 1)

# input
N = int(input())
print(recurrance(N))