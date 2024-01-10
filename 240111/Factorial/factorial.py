def factorial(n: int) -> int:
    if n <= 1: return 1
    return n * factorial(n -1)


# input
n = int(input())
result: int = factorial(n)
print(result)