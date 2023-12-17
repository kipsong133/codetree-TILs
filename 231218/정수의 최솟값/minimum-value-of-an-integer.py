# 세 개의 정수를 입력받는다.
a, b ,c = tuple(map(int, input().split()))

def find_minimum(*args) -> int:
    minimum_value = args[0]
    for num in args:
        if minimum_value > num:
            minimum_value = num
    return minimum_value

result = find_minimum(a, b, c)
print(result)