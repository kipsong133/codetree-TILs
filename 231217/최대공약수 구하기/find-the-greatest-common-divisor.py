import math

def finding_divisor(num: int):
    result = set([]) # 중복제거를 위해, Set을 이용한다.
    
    # 제곱까지만 순회한다.
    sqrt_num = int(math.sqrt(num))
    
    for i in range(1, sqrt_num + 1):
        divisor = num % i # 3
        if divisor == 0:
            result.add(i)
            result.add(num // i)
    return result

def solution():
    # Input: 12, 18
    input_arr = list(map(int, input().split()))
    n, m = input_arr[0], input_arr[1]
    
    # 최대 공약수
    # 약수 구하기
    divisor_n = finding_divisor(n)
    divisor_m = finding_divisor(m)

    # 교집합 찾기
    result = divisor_n & divisor_m
    print(max(result))

solution()