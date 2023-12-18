# input: 5 19
a, b = tuple(map(int, input().split()))

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

result = 0
# sum prime numbers between 5 and 19
for i in range(a, b + 1):
    if is_prime(i):
        result += i
print(result)