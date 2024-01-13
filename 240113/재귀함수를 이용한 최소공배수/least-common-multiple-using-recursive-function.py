def gcd(x, y):
    """두 수의 최대공약수를 구하는 함수"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    """두 수의 최소공배수를 구하는 함수"""
    return x * y // gcd(x, y)

def lcm_multiple(numbers, index=0):
    """재귀를 사용하여 여러 수의 최소공배수를 구하는 함수"""
    if index == len(numbers) - 1:
        return numbers[index]
    else:
        return lcm(numbers[index], lcm_multiple(numbers, index + 1))

count = int(input())
numbers = list(map(int, input().split()))
result = lcm_multiple(numbers)
print(result)